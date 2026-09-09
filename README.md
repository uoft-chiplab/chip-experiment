This project turns Markdown files into a website-ready wiki-style documentation site using mkdocs. The idea is that the user locally makes their changes and then commits them. Pushing to `main` runs the GitHub Actions workflow in `.github/workflows/deploy.yml`, which builds the site and publishes it to https://uoft-chiplab.github.io/chip-experiment/. Pull requests get a build-only check. The `gh-pages` branch is no longer used.

If after a minute the website has not changed upon refresh, the build might have failed. See https://github.com/uoft-chiplab/chip-experiment/actions for the log, or press "Run workflow" there to redeploy by hand.

See requirements.txt for necessary installs only if you want to build the site manually using mkdocs (`pip install -r requirements.txt`, then `mkdocs serve`).

To customize the order of files and folders on the website, modify the .pages file.

To adjust global settings, look at the YAML source files.

## Embedding a Google Sheet

Lab sheets stay private. A page can embed a tab live with `{{ gsheet <name> }}`, where `<name>` is registered in `SHEETS` in `hooks.py` (one line: spreadsheet id and tab gid, both read off the sheet's URL). Viewers must be signed into a Google account the sheet is shared with; everyone else sees an access prompt. Never use *Publish to web* on a sheet: it is not needed and makes the tab public. See the Calibrations page for a working example and troubleshooting table.
