# Calibrations

Calibration data lives in the lab's private Google Sheets and is embedded here live.
Nothing is copied into the wiki: the embedded frame talks to Google directly, so you
must be **signed into a Google account the sheet is shared with** in this browser.
Anyone else sees an access prompt instead of the data.

## Embed test

This page doubles as the test case for sheet embedding. Both frames below show the same
tab (ODT1/2) using the two URL forms Google allows in an iframe. If either renders the
table, the embedding works.

### Preview mode (read-only, default)

{{ gsheet odt-calibration }}

### Edit mode (`mode=edit`, minimal toolbar, editable by anyone with edit rights)

{{ gsheet odt-calibration mode=edit height=300 }}

### What you should see

| What you see | Meaning |
|---|---|
| **The ODT1/2 table with dates and values** | **PASS.** Embedding works in this browser. |
| A Google sign-in prompt inside the frame | You are not signed into Google. Sign in, then reload. |
| "You need access" | You are signed in with an account the sheet is not shared with. Ask a lab member to share it. |
| A blank or grey frame, or a sign-in prompt that keeps reappearing | Your browser blocks third-party cookies (Safari by default, Firefox in strict mode, Brave). Use the "Open in Google Sheets" link under the frame, or allow cookies for `docs.google.com`. |

## Adding a sheet to a page

1. Add one line to `SHEETS` in `hooks.py` at the repo root, mapping a short name to the
   spreadsheet id and tab gid (both are in the sheet's URL: `.../d/<id>/edit?gid=<gid>`).
2. In the page, write `{{ gsheet <name> }}`. Options: `height=600`, `mode=edit`.
3. Keep the sheet's sharing set to *Restricted* with lab members added. Do **not** use
   *Publish to web*; it is not needed and would make the tab public.

Last updated September 2026
