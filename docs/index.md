# Overview

A central repository for chip-lab-related physics and technical knowledge. This is intended to be a unifying reference for all aspects of the experiment that can be edited freely and easily updated.

Built with mkdocs; for full documentation visit [mkdocs.org](https://www.mkdocs.org).

## How to use
* Clone the git repo at https://github.com/uoft-chiplab/chip-experiment.git
* Write Markdown files inside docs/. 
* Commit and push to main. A workflow script (.github/workflows/ci.yml) should auto-deploy and build the .md files into a searchable website using GitHub Pages at https://uoft-chiplab.github.io/chip-experiment/
* You may need to wait a few minutes and refresh your browser cache to see updates. (Windows: `Ctrl + F5`, Mac: `Cmd + Shift + R`)

Manual mkdocs commands that might be helpful include:

* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        subfolder/
            overview.md # for quick summaries, contexts, and review
            specific-information.md
            imgs/ 
        ...       # Other markdown pages, images and other files.

## Other info
Ordering is alphanumeric by default. Override this by adding a file named .pages written like a yaml. This uses the awesome-pages-plugin. Each folder needs its own .pages file. For this homepage, the folders reflect the general sequence of the experiment. Ex:

    nav:
    - index.md
    - useful-relations.md
    - apparatus
    - laser-cooling
    - optical-pumping
    - magnetic-trapping
    - optical-dipole-trapping
    - state-preparation
    - imaging
    - thermometry