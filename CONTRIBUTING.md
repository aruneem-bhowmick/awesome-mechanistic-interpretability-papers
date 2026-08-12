# Contributing

This list is intentionally curated and ordered (foundational → advanced), not an exhaustive dump. Before opening a PR:

1. **Pick the right section.** If a paper genuinely bridges two sections (like grokking papers bridging Circuits and Training Dynamics), cross-list it rather than forcing one bucket.
2. **Justify placement, not just inclusion.** Add a one-line "why it matters" that explains what the paper adds *relative to what's already in that section* — not just a restated abstract.
3. **Respect the ordering.** Within a section, earlier rows should be prerequisites (conceptually or historically) for later rows.
4. **No orphan additions.** If you add a paper, either add an entry to the matching `notes/NN-section.md` file or leave a `TODO` there so the index and the notes don't drift apart.
5. **Ten-per-section is a ceiling, not a quota.** `README.md` tables aim for around 10 curated papers per section, but that's a cap on how much a section grows, not a target to force. Don't pad a section with a marginal pick just to hit the number — and be wary of adding very recent, uncited preprints straight to the core table; if a paper is solid but hasn't earned a core slot yet (often simply because it's too new to have a track record), it belongs in `extended-reading/NN-section.md` instead.

## Extended reading

Each section in `README.md` (§2–§9) has a companion `extended-reading/NN-section.md` file, mirroring the `notes/NN-section.md` naming. It holds papers that are on-topic and reasonably solid but didn't clear the bar for the curated top-10 — usually because they're recent preprints without a track record yet, cover narrower or more applied ground than the core list, or are redundant with a stronger pick already in the table. Unlike `notes/`, extended-reading entries don't need a matching notes-file entry. Promote an entry from `extended-reading/` into `README.md` (and add its notes) if it proves out over time.

For reordering or restructuring proposals (e.g., splitting a section, renumbering), open an issue first rather than a PR — the numbering is referenced from the README's suggested reading order and from file names under `notes/` and `extended-reading/`, so structural changes touch multiple files.
