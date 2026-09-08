This project turns Markdown files into a website-ready wiki-style documentation site using mkdocs. The idea is that the user locally makes their changes and then commits them. Upon commit, a GitHub Pages bot will automatically build everything into website-readable HTML at https://uoft-chiplab.github.io/chip-experiment/. The bot was set up in the .github/workflows folder with some GitHub settings. The build should fire only when committing to main; do not commit to the bot branch gh-pages.

See requirements.txt for necessary installs only if you want to build the site manually using mkdocs.

To customize the order of files and folders on the website, modify the .pages file.

To adjust global settings, look at the YAML source files.