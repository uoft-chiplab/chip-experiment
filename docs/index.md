# Chip Experiment Docs

A central repository for chip-lab-related physics and technical knowledge. This is intended to be a unifying reference for all aspects of the experiment that can be edited freely and easily updated.

Built with mkdocs; for full documentation visit [mkdocs.org](https://www.mkdocs.org).

## How to use
* Clone the git repo at https://github.com/uoft-chiplab/chip-experiment.git
* Write Markdown files inside docs/. 
* Commit and push to main. A workflow script (.github/workflows/ci.yml) should auto-deploy and build the .md files into a searchable website using GitHub Pages at https://uoft-chiplab.github.io/chip-experiment/
* You may need to refresh your browser cache to see updates. (Windows: `Ctrl + F5`, Mac: `Cmd + Shift + R`)

Manual mkdocs commands that might be helpful include:
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        useful-relations.md # Table of important relations.
        apparatus/
            overview.md
            magnetic-coils.md
            optical-diagrams.md
            imgs/
        laser-cooling/
            overview.md
            MOT.md
            molasses.md
            gray-molasses.md

        optical-pumping/
            optical-pumping.md
        magnetic-trapping/
            quadrupole-magnetic-trap.md
            magnetic-transfer.md
            chip-trap.md
            forced-rf-evaporation.md
        optical-dipole-trap/
            optical-trapping.md
            optical-evaporation.md
        imaging/
            imaging.md
        thermometry/
            noninteracting-ballistic-expansion.md
            unitary-expansion.md

        ...       # Other markdown pages, images and other files.
