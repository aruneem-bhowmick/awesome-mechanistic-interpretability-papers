# Scripts

## `fetch_papers.py`

Pulls recent arXiv papers into `PAPER-INBOX.md` for manual triage. Curation stays
manual — see [CONTRIBUTING.md](../CONTRIBUTING.md) — this script only surfaces
candidates so you don't have to search arXiv by hand.

Python 3, stdlib only. No dependencies to install.

```
python scripts/fetch_papers.py                    # all sections
python scripts/fetch_papers.py --section 03        # just one section (prefix match ok)
python scripts/fetch_papers.py --max-per-section 10
python scripts/fetch_papers.py --dry-run           # print candidates, write nothing
```

Runs one arXiv query per README section (sections 2–9; 1 and 10 are editorial calls,
not queryable). Results are deduped two ways:

- Against `README.md`'s existing tables (by normalized title), so already-curated
  papers never reappear as candidates.
- Against `seen_arxiv_ids.txt` (below), so a paper you've already triaged — accepted
  *or* rejected — never comes back.

New candidates are appended to `PAPER-INBOX.md` under the matching section header,
without touching anything already there — check-marks and manual notes survive a
re-run.

## `seen_arxiv_ids.txt`

Flat, sorted, one arXiv id per line, git-committed. Every id ever written to
`PAPER-INBOX.md` lives here. This is what makes rejection permanent: delete an entry
from `PAPER-INBOX.md` and it will not resurface on a later run, because the id stays
in this file regardless of what happened to the entry itself.

## Not built yet

A scheduled GitHub Action (weekly cron, runs `fetch_papers.py`, opens a PR via
`peter-evans/create-pull-request` if `PAPER-INBOX.md` changed) is deliberately
deferred. It's follow-up work once the section queries in `SECTION_QUERIES` have been
run manually a few times and their signal/noise ratio is trusted — tune the queries
first, automate second.
