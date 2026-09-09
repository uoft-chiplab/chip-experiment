"""MkDocs hook: expand `{{ gsheet <name> [height=N] [mode=preview|edit] }}` into a
Google Sheets iframe.

Sheets stay private on the Google side. The viewer's own Google login gates
access, so nothing is fetched or exported at build time. To make a new tab
available, add one line to SHEETS below (spreadsheet id + tab gid, both taken
from the sheet's URL: .../d/<id>/edit?gid=<gid>).
"""
import re

SHEETS = {  # name -> (spreadsheet id, gid)
    "odt-calibration": ("1qCv8nCcFE9Q4doqnjptF11CEoNVKVvIUh7oMNYdZbDk", "1029283282"),
}

DEFAULT_HEIGHT = 450
_RE = re.compile(r"\{\{\s*gsheet\s+([\w-]+)((?:\s+\w+=\S+)*)\s*\}\}")


def _render(name, opts, page):
    try:
        sid, gid = SHEETS[name]
    except KeyError:
        raise KeyError(
            f"{page.file.src_path}: unknown sheet '{name}'. "
            f"Known names: {', '.join(sorted(SHEETS))}. Add it to SHEETS in hooks.py."
        )
    height = opts.get("height", DEFAULT_HEIGHT)
    mode = opts.get("mode", "preview")  # preview (read-only) | edit (rm=minimal)
    if mode == "edit":
        src = f"https://docs.google.com/spreadsheets/d/{sid}/edit?gid={gid}&rm=minimal"
    elif mode == "preview":
        src = f"https://docs.google.com/spreadsheets/d/{sid}/preview?gid={gid}"
    else:
        raise ValueError(f"{page.file.src_path}: gsheet mode must be 'preview' or 'edit', got '{mode}'")
    open_url = f"https://docs.google.com/spreadsheets/d/{sid}/edit?gid={gid}"
    return (
        f'<div class="gsheet" markdown="0">'
        f'<iframe src="{src}" height="{height}" loading="lazy" title="Google Sheet: {name}"></iframe>'
        f'<p class="gsheet-fallback"><a href="{open_url}" target="_blank" rel="noopener">'
        f'Open in Google Sheets &#8599;</a> (lab Google account required)</p>'
        f'</div>'
    )


def on_page_markdown(markdown, page, config, files):
    def sub(m):
        opts = dict(kv.split("=", 1) for kv in m.group(2).split())
        return _render(m.group(1), opts, page)

    return _RE.sub(sub, markdown)
