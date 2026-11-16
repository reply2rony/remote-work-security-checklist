# Remote Work Security Checklist

A starter learning template for keeping remote work secure:
the devices people work on, the home networks they connect
from, the accounts they sign in with, and how work data is
handled and switched off. It comes with a starter script that
summarises how far through the list you are. It is a learning
template with fictional sample data only. It is not a
production tool, it makes no claim about any real
organisation, and it contains no real company data and no
invented metrics.

## What it is

- `docs/remote-work-guide.md` — the guide: what remote work
  security means at this level, how to work through the
  checklist, and the checks to run before trusting it.
- `remote-work-security-checklist.csv` — a small fictional
  sample checklist: 14 made-up items across 6 categories, so
  you can run the script and see the shape of the output.
- `scripts/remote-work-summary.py` — a starter Python script
  that reads a CSV in the sample shape and prints the counts
  by status and by category, the percentage complete, and the
  high-priority items still outstanding. Labelled a starter
  learning template; it is not a production tool.

## How to use

1. Read `docs/remote-work-guide.md` first — it explains the
   categories and how to work the list in order.
2. Run the script on the sample data:

```bash
python3 scripts/remote-work-summary.py remote-work-security-checklist.csv
```

3. Copy the sample CSV, replace the sample rows with your own
   checklist items for your own systems, and re-run the script
   to see your own progress. Never put real system names,
   addresses, or credentials in the file.
4. Work the high-priority items first, and re-run the script
   after each change so the percentage stays honest.

## What the sample output looks like

Running the script on the sample file gives, for the 14
fictional items:

- Done: 6 of 14 (42.9% complete)
- In progress: 5, Not started: 3
- By category: Devices 3, Home network 3, Accounts 2,
  Data handling 2, Communication 2, Offboarding 2
- Outstanding high-priority items: 3 — "Change the home
  router admin password from the default" (In progress),
  "Never email work files to personal accounts" (Not started)
  and "Verify unexpected payment or credential requests by a
  second channel" (Not started)

Those numbers come from the fictional sample rows in the CSV,
not from any real organisation. Recount them yourself with the
script — that is the point of the exercise.

## Sample / Demo notice

All items, categories, owners, and notes in this repo are
fictional samples for learning. The diagram in
`docs/diagram.png` is a locally generated illustration labelled
"Sample / Demo" — it is not a screenshot of a real system, and
this template does not claim any production use.

## License

MIT — see `LICENSE`.
