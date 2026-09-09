# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A MkDocs (Material theme) documentation wiki for the UofT chip lab's cold-atom experiment (Rb-87 / K-40). Almost all content is Markdown in `docs/`; the only Python is `hooks.py`. There are no tests and no linter.

The audience is students: pages should prioritize intuition over derivation, and link out for long derivations rather than inlining them (see `docs/index.md` goals).

## Commands

```bash
pip install -r requirements.txt   # only needed for local builds
mkdocs serve                      # live-reloading preview at localhost:8000
mkdocs build --strict             # what CI runs; warnings are failures
```

## Deployment

Pushing to `main` triggers `.github/workflows/deploy.yml`: it installs `requirements.txt`, runs `mkdocs build --strict`, and publishes via `actions/upload-pages-artifact` + `actions/deploy-pages` to https://uoft-chiplab.github.io/chip-experiment/. Pull requests run the build job only. The repo's Pages source must be set to "GitHub Actions" (Settings > Pages). The old `gh-pages` branch is unused and can be deleted. If the site doesn't update, check https://github.com/uoft-chiplab/chip-experiment/actions (and hard-refresh); "Run workflow" there redeploys manually.

CI installs from `requirements.txt`, so **any new mkdocs plugin or Python import must be added in two places: `mkdocs.yml` and `requirements.txt`.** `--strict` turns MkDocs warnings (broken links, pages missing from nav) into build failures, so run `mkdocs build --strict` locally before pushing.

`site/` is local build output and is gitignored; the workflow builds fresh on every deploy.

## Navigation ordering

Ordering is alphanumeric unless a folder contains a `.pages` file (mkdocs-awesome-pages-plugin). Each folder needs its own `.pages`; a trailing `- ...` entry means "everything else, alphanumeric". `docs/.pages` orders the top-level sections to follow the physical sequence of the experiment (apparatus > laser-cooling > optical-pumping > magnetic-trapping > optical-dipole-trapping > state-preparation > imaging > thermometry), so a new section belongs at its point in that sequence, not appended.

Convention: each section folder has an `overview.md` (summary/context) first, then specific pages, plus an `imgs/` subfolder for its figures.

## Markdown conventions

- **Math**: `pymdownx.arithmatex` in generic mode plus MathJax (`docs/javascripts/mathjax.js`). Write `$...$` inline and `$$...$$` display; arithmatex rewrites them to the `\(...\)` / `\[...\]` delimiters MathJax is configured for.
- **Figures**: `attr_list` + `md_in_html` are enabled, so use the Material pattern:
  ```markdown
  <figure markdown>
    ![alt](imgs/foo.png){ width="400" }
    Caption text, which may contain $math$.
  </figure>
  ```
- **Tables** are plain Markdown and routinely carry math and multi-line cells (`<br>`); see `docs/useful-relations.md` and `docs/laser-cooling/MOT.md` for the house style (bolded row label, units in the header).
- Experimental parameter tables should carry a "Last updated <Month Year>" line, as in `docs/laser-cooling/MOT.md`.

## Google Sheets embeds (hooks.py)

Lab sheets are private and the site is public, so sheet data is never fetched or exported at build time. Instead `hooks.py` is an `on_page_markdown` hook that expands `{{ gsheet <name> }}` (options `height=N`, `mode=preview|edit`) into an iframe of the Google Sheet; the viewer's own Google login gates access. `SHEETS` in `hooks.py` maps a short name to `(spreadsheet id, gid)`; adding a tab means adding one line there. Unknown names fail the build with a message listing known names. Styling lives in `docs/stylesheets/extra.css`. `docs/calibrations/overview.md` is the reference example and troubleshooting table. Never suggest "Publish to web" for a sheet.
