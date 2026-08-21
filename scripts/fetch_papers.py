#!/usr/bin/env python3
"""Pull recent arXiv papers per README section into PAPER-INBOX.md for manual triage.

Curation stays manual (see CONTRIBUTING.md) — this script only surfaces candidates.
"""

import argparse
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
README_PATH = ROOT / "README.md"
INBOX_PATH = ROOT / "PAPER-INBOX.md"
SEEN_IDS_PATH = Path(__file__).resolve().parent / "seen_arxiv_ids.txt"

ARXIV_API = "http://export.arxiv.org/api/query"
USER_AGENT = (
    "awesome-mechanistic-interpretability-papers-fetch-bot/1.0 "
    "(+https://github.com/aruneem-bhowmick/awesome-mechanistic-interpretability-papers)"
)
ATOM_NS = "{http://www.w3.org/2005/Atom}"
CATEGORY_FILTER = "(cat:cs.LG OR cat:cs.CL OR cat:cs.AI OR cat:cs.NE)"
REQUEST_DELAY_SECONDS = 3

# Sections 1 (Foundations & Philosophy) and 10 (Surveys & Reviews) are deliberately
# excluded: deciding what's foundational or survey-worthy is an editorial call a
# keyword query can't make. Keys match the `notes/NN-*` filenames.
SECTION_QUERIES = {
    "02-circuits-and-features": (
        "Circuits & Features",
        'abs:"circuit discovery" OR abs:"attention circuit" '
        'OR (abs:"circuit analysis" AND abs:"interpretability")',
    ),
    "03-superposition-and-saes": (
        "Superposition & Sparse Autoencoders",
        'abs:"sparse autoencoder" '
        'OR (abs:"dictionary learning" AND (abs:"language model" OR abs:"interpretability")) '
        'OR (abs:"superposition" AND (abs:"neural network" OR abs:"language model" OR abs:"feature"))',
    ),
    "04-representation-geometry": (
        "Representation Geometry & Linear Structure",
        'abs:"linear representation hypothesis" OR abs:"representation geometry" '
        'OR abs:"emergent world representation" '
        'OR (abs:"linear probe" AND abs:"interpretability")',
    ),
    "05-causal-methods": (
        "Causal Methods: Patching, Ablation, Editing",
        'abs:"activation patching" OR abs:"causal tracing" OR abs:"activation steering" '
        'OR abs:"model editing"',
    ),
    "06-in-context-learning": (
        "In-Context Learning & Attention Circuits",
        'abs:"induction head" OR abs:"function vector" '
        'OR (abs:"in-context learning" AND abs:"mechanistic")',
    ),
    "07-training-dynamics-and-grokking": (
        "Training Dynamics & Grokking",
        'abs:"grokking" AND (abs:"generalization" OR abs:"training dynamics" '
        'OR abs:"double descent" OR abs:"modular arithmetic" OR abs:"phase transition")',
    ),
    "08-scaling-and-automated-interp": (
        "Scaling Interpretability & Automated Interp",
        '(abs:"automated interpretability" OR abs:"scaling interpretability" '
        'OR abs:"autointerp" OR abs:"neuron explanation") '
        'AND (abs:"language model" OR abs:"neural network" OR abs:"transformer")',
    ),
    "09-applications-safety": (
        "Applications: Safety, Steering, Unlearning",
        'abs:"representation engineering" OR abs:"machine unlearning" '
        'OR abs:"refusal direction" OR abs:"activation addition"',
    ),
}

# Client-side literal-phrase confirmation, keyed like SECTION_QUERIES. arXiv's
# legacy export.arxiv.org/api/query endpoint has been observed (issue #3) not to
# reliably enforce phrase co-occurrence for multi-clause AND/OR search_query
# strings server-side, so sections whose noise didn't improve after tightening
# the query re-check the actual returned abstract text here before accepting.
SECTION_POST_FILTERS = {
    "02-circuits-and-features": lambda abstract: (
        "circuit discovery" in abstract
        or "attention circuit" in abstract
        or ("circuit analysis" in abstract and "interpretability" in abstract)
    ),
    "03-superposition-and-saes": lambda abstract: (
        "sparse autoencoder" in abstract
        or (
            "dictionary learning" in abstract
            and any(term in abstract for term in ("language model", "interpretability"))
        )
        or (
            "superposition" in abstract
            and any(
                term in abstract
                for term in ("neural network", "language model", "feature")
            )
        )
    ),
    "04-representation-geometry": lambda abstract: (
        "linear representation hypothesis" in abstract
        or "representation geometry" in abstract
        or "emergent world representation" in abstract
        or ("linear probe" in abstract and "interpretability" in abstract)
    ),
    "05-causal-methods": lambda abstract: any(
        term in abstract
        for term in (
            "activation patching",
            "causal tracing",
            "activation steering",
            "model editing",
        )
    ),
    "07-training-dynamics-and-grokking": lambda abstract: (
        "grokking" in abstract
        and any(
            term in abstract
            for term in (
                "generalization",
                "training dynamic",
                "double descent",
                "modular arithmetic",
                "phase transition",
            )
        )
    ),
    "08-scaling-and-automated-interp": lambda abstract: (
        any(
            term in abstract
            for term in (
                "automated interpretability",
                "scaling interpretability",
                "autointerp",
                "neuron explanation",
            )
        )
        and any(
            term in abstract
            for term in ("language model", "neural network", "transformer")
        )
    ),
}

DEFAULT_PREAMBLE = """# Paper Inbox

This is a staging area for arXiv papers pulled automatically by `scripts/fetch_papers.py`.
Nothing here has been reviewed yet.

To triage an entry:
- **Accept**: move it into `README.md` under the matching section, add a line to the
  matching `notes/NN-*.md` file (see [CONTRIBUTING.md](CONTRIBUTING.md)), then delete
  the entry here.
- **Reject**: delete the entry here. It will not come back — every id pulled into this
  file is recorded in `scripts/seen_arxiv_ids.txt`, so a rejected paper won't resurface
  on a later run."""

SECTION_HEADER_RE = re.compile(r"^###\s+(\d+)\.\s+(.+?)\s*$", re.MULTILINE)
ENTRY_START_RE = re.compile(r"^- \[[ xX]\] ", re.MULTILINE)
NON_ALNUM_RE = re.compile(r"[^a-z0-9\s]")
WHITESPACE_RE = re.compile(r"\s+")


def parse_args():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--section",
        help="Only fetch this section, e.g. '03' or '03-superposition-and-saes'.",
    )
    parser.add_argument(
        "--max-per-section",
        type=int,
        default=20,
        help="Max results per section query (default: 20).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print candidates without writing PAPER-INBOX.md or updating the seen-ids log.",
    )
    return parser.parse_args()


def select_sections(section_arg):
    items = list(SECTION_QUERIES.items())
    if not section_arg:
        return items
    if section_arg in SECTION_QUERIES:
        return [(section_arg, SECTION_QUERIES[section_arg])]
    matches = [k for k in SECTION_QUERIES if k.startswith(section_arg)]
    if len(matches) != 1:
        raise SystemExit(
            f"Unknown or ambiguous section {section_arg!r}. Known: {', '.join(SECTION_QUERIES)}"
        )
    return [(matches[0], SECTION_QUERIES[matches[0]])]


def normalize_title(title):
    t = title.lower()
    t = NON_ALNUM_RE.sub("", t)
    t = WHITESPACE_RE.sub(" ", t).strip()
    return t


def load_existing_titles(readme_path):
    titles = set()
    for line in readme_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if not cells or not cells[0]:
            continue
        first = cells[0]
        if first in ("Paper", "Tool") or set(first) <= {"-", ":"}:
            continue
        titles.add(normalize_title(first))
    return titles


def load_seen_ids(path):
    if not path.exists():
        return set()
    return {line.strip() for line in path.read_text(encoding="utf-8").splitlines() if line.strip()}


def save_seen_ids(path, ids):
    path.write_text("\n".join(sorted(ids)) + "\n", encoding="utf-8")


def build_query(phrase_query):
    return f"({phrase_query}) AND {CATEGORY_FILTER}"


def truncate(text, limit):
    if len(text) <= limit:
        return text
    cut = text[:limit].rsplit(" ", 1)[0]
    return cut + "…"


def format_authors(authors):
    if not authors:
        return "Unknown"
    last_names = [a.split()[-1] if a.split() else a for a in authors]
    if len(last_names) > 5:
        return ", ".join(last_names[:5]) + ", et al."
    return ", ".join(last_names)


def parse_entry(entry):
    raw_id = entry.findtext(f"{ATOM_NS}id", default="")
    short_id = re.sub(r"^https?://arxiv\.org/abs/", "", raw_id)
    short_id = re.sub(r"v\d+$", "", short_id)

    title = " ".join(entry.findtext(f"{ATOM_NS}title", default="").split())
    authors = [
        " ".join(a.findtext(f"{ATOM_NS}name", default="").split())
        for a in entry.findall(f"{ATOM_NS}author")
    ]
    published = entry.findtext(f"{ATOM_NS}published", default="")
    year = published[:4] if published else "n.d."
    summary = " ".join(entry.findtext(f"{ATOM_NS}summary", default="").split())

    return {
        "id": short_id,
        "title": title,
        "authors": authors,
        "year": year,
        "abstract": truncate(summary, 220),
        "abstract_full": summary,
    }


def fetch_section(query, max_results):
    params = {
        "search_query": query,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
        "max_results": str(max_results),
    }
    url = f"{ARXIV_API}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()
    root = ET.fromstring(data)
    return [parse_entry(entry) for entry in root.findall(f"{ATOM_NS}entry")]


def format_entry(record, today):
    authors = format_authors(record["authors"])
    return (
        f"- [ ] **{record['title']}** — {authors} ({record['year']})\n"
        f"  arXiv:{record['id']} · <https://arxiv.org/abs/{record['id']}>\n"
        f"  > {record['abstract']}\n"
        f"  _Pulled: {today}_"
    )


def split_entries(body):
    starts = [m.start() for m in ENTRY_START_RE.finditer(body)]
    return [
        body[start : (starts[i + 1] if i + 1 < len(starts) else len(body))].rstrip("\n")
        for i, start in enumerate(starts)
    ]


def parse_inbox(text):
    headers = list(SECTION_HEADER_RE.finditer(text))
    if not headers:
        return text.rstrip("\n"), {}
    preamble = text[: headers[0].start()].rstrip("\n")
    sections = {}
    for i, m in enumerate(headers):
        num = int(m.group(1))
        title = m.group(2)
        body_start = m.end()
        body_end = headers[i + 1].start() if i + 1 < len(headers) else len(text)
        sections[num] = (title, split_entries(text[body_start:body_end]))
    return preamble, sections


def render_inbox(preamble, sections):
    parts = [preamble.rstrip("\n"), ""]
    for num in sorted(sections):
        title, entries = sections[num]
        parts.append(f"### {num}. {title}")
        parts.append("")
        for entry in entries:
            parts.append(entry)
            parts.append("")
        parts.append("---")
        parts.append("")
    return "\n".join(parts).rstrip("\n") + "\n"


def write_inbox(new_entries_by_section, today):
    if INBOX_PATH.exists():
        preamble, sections = parse_inbox(INBOX_PATH.read_text(encoding="utf-8"))
    else:
        preamble, sections = DEFAULT_PREAMBLE, {}

    for section_num, (title, records) in new_entries_by_section.items():
        existing_title, entries = sections.get(section_num, (title, []))
        entries.extend(format_entry(r, today) for r in records)
        sections[section_num] = (existing_title, entries)

    INBOX_PATH.write_text(render_inbox(preamble, sections), encoding="utf-8")


def print_dry_run(new_entries_by_section):
    if not new_entries_by_section:
        print("No new candidates.")
        return
    for section_num in sorted(new_entries_by_section):
        title, records = new_entries_by_section[section_num]
        print(f"\n### {section_num}. {title}  ({len(records)} candidate(s))")
        for r in records:
            print(f"  - {r['title']} — {format_authors(r['authors'])} ({r['year']}) [arXiv:{r['id']}]")


def main():
    args = parse_args()
    sections = select_sections(args.section)
    existing_titles = load_existing_titles(README_PATH)
    seen_ids = load_seen_ids(SEEN_IDS_PATH)
    run_seen_ids = set()
    today = datetime.now().strftime("%Y-%m-%d")

    new_entries_by_section = {}
    for i, (key, (title, phrase_query)) in enumerate(sections):
        section_num = int(key.split("-")[0])
        query = build_query(phrase_query)
        post_filter = SECTION_POST_FILTERS.get(key)
        try:
            records = fetch_section(query, args.max_per_section)
        except (urllib.error.URLError, OSError, ET.ParseError) as exc:
            print(f"Warning: failed to fetch section {key}: {exc}")
            records = []

        accepted = []
        for record in records:
            if normalize_title(record["title"]) in existing_titles:
                continue
            if record["id"] in seen_ids or record["id"] in run_seen_ids:
                continue
            if post_filter and not post_filter(record["abstract_full"].lower()):
                continue
            run_seen_ids.add(record["id"])
            accepted.append(record)

        if accepted:
            new_entries_by_section[section_num] = (title, accepted)

        if i < len(sections) - 1:
            time.sleep(REQUEST_DELAY_SECONDS)

    total = sum(len(records) for _, records in new_entries_by_section.values())

    if args.dry_run:
        print_dry_run(new_entries_by_section)
        print(f"\n{total} new candidate(s) found (dry run — nothing written).")
        return

    if total == 0:
        print("No new candidates found.")
        return

    write_inbox(new_entries_by_section, today)
    save_seen_ids(SEEN_IDS_PATH, seen_ids | run_seen_ids)
    print(f"Wrote {total} new candidate(s) to {INBOX_PATH.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
