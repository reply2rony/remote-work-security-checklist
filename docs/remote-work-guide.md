# Remote Work Security — Starter Guide

A starter guide to remote work security for a small office:
the devices people work on at home, the home networks they
connect from, the accounts they sign in with, how work data
is handled, and how access is switched off. This guide
explains the shape of the work and the checks to run. All
examples are fictional samples for learning. This template
does not describe any real organisation, real systems, or
production use.

## What remote work security means here

Working from home moves the office boundary onto kitchen
tables, home routers, and personal Wi-Fi — so the checklist
covers the whole chain, not just one part. A locked laptop
means little on an open home network, and a strong password
means little if work files are emailed to a personal inbox.
None of the items in the sample checklist is advanced — each
one is a small, checkable step, and the whole list is meant
to be worked through in order, highest priority first. The
script in this repo, `scripts/remote-work-summary.py`, is a
starter example of how to track that work: it reads the
checklist CSV and prints the counts by status and by
category, the percentage complete, and the high-priority
items still outstanding.

## The checklist shape

The script expects a CSV with these columns:

| Column | Meaning | Example (fictional) |
|--------|---------|---------------------|
| item | The step to do | Require multi-factor sign-in for work accounts |
| category | Which area it belongs to | Accounts |
| status | Done, In progress, or Not started | Done |
| priority | High, Medium, or Low | High |
| owner | Who is responsible (sample names only) | Sample owner - IT lead |
| note | A short human note (optional) | Sample item - second factor on every work sign-in |

Keep the shape fixed: same column names, same order, one row
per step, and only the three exact status values — the script
rejects anything else so a typo cannot silently become a
"done" item.

## The six categories

1. **Devices** — the laptops and phones work happens on.
   Full-disk encryption on every work laptop, patches applied
   within 14 days, and the screen locking itself after 5
   minutes idle. A lost or unattended device is the most
   ordinary way work data walks away.
2. **Home network** — the connection between the device and
   the office. The company VPN on public Wi-Fi, the home
   router admin password changed from its default, and home
   Wi-Fi on WPA2 or WPA3 with a strong password. The default
   router password is public knowledge — change it.
3. **Accounts** — how people sign in. Multi-factor sign-in
   on every work account, and a password manager so no
   password is ever reused. One leaked password should never
   open a second account.
4. **Data handling** — where work files live. Work files only
   in approved cloud storage, and never emailed to personal
   accounts — a personal inbox is outside the organisation's
   control, and files sent there do not come back.
5. **Communication** — how people talk and verify. Video
   calls on approved tools only, and any unexpected payment
   or credential request verified through a second channel —
   call back on a known number before acting.
6. **Offboarding** — switching it all off. Work devices
   returned or wiped on the last day, and remote access
   revoked the same day someone leaves. Access that outlives
   the job is a way back in.

## Working the list

1. **Copy the sample CSV** and replace the sample rows with
   your own items for your own systems. Never put real system
   names, addresses, or credentials in the file.
2. **Run the script** to see where the list stands:
   `python3 scripts/remote-work-summary.py remote-work-security-checklist.csv`
3. **Do the high-priority items first.** The script lists the
   outstanding high-priority items at the bottom — that is
   your next work, in order.
4. **Mark an item Done only when it is actually done** — not
   when it is planned. Change the status in the CSV, re-run
   the script, and check the percentage moved.
5. **Review monthly.** A checklist rots fast: people join and
   leave, routers get replaced, devices change hands. Re-run
   the script each month and add or retire rows as the systems
   change.

## Checks that catch real mistakes

- **Status spelling.** Only `Done`, `In progress`, and `Not
  started` are accepted. The script stops on anything else,
  so a typo like "done" or "In-progress" is caught instead of
  silently counted as nothing.
- **Two cuts must agree.** The counts by status and the counts
  by category must both add up to the same total. In the
  sample data: Done 6 + In progress 5 + Not started 3 = 14,
  and Devices 3 + Home network 3 + Accounts 2 + Data handling
  2 + Communication 2 + Offboarding 2 = 14. If the two cuts
  disagree, a row is miscategorised or missing.
- **High-priority first.** If a high-priority item has sat
  "Not started" for a month, that is the finding — say so
  plainly instead of letting the percentage hide it.
- **Verify, do not assume.** Walk the list against the real
  systems: check that encryption is actually on, that the
  router password was actually changed, that the leaver's
  access is actually gone. A tick in a spreadsheet is not a
  test.

## What this template does not do

- It does not change any system itself — it only tracks the
  checklist. Every item is done by hand, in your own systems,
  by someone with the right access.
- It does not scan, audit, or test your network. If you need
  a scan, use your organisation's own approved tools.
- It does not store credentials, keys, or system addresses.
  Those belong in your organisation's own secure store, never
  in a repo.

## Sample / Demo notice

All items, categories, owners, and notes in this repo are
fictional samples for learning. The diagram in
`docs/diagram.png` is a locally generated illustration labelled
"Sample / Demo" — it is not a screenshot of a real system, and
this template does not claim any production use.
