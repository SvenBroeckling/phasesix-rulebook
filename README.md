## PhaseSix and Tirakans Reiche Rulebook

These documents are the source for the role-playing games PhaseSix, NEXUS and Tirakans Reiche.

The documents are divided into three parts:

* The rules
* The character sheet
* The appendix documents

The rules are static LaTeX documents in the `chapters` directory. The character sheet is a separate LaTeX document in the `character-sheet` directory. The appendix documents are rendered with python jinja2 from the game data from the website `phasesix.org`.

The rulebook documents are built with the `build` script in the root directory. To run the script and install the dependencies, `uv` is used.

### Project structure

* `build`: Build script
* `document-body.tex`: The main LaTeX document body
* `main-online.tex`: Entrypoint script for online build
* `main-print.tex`: Entrypoint script for print build
* `utils`: LaTeX utilities for internationalization and the management of different world books
* `chapters`: The LaTeX source for the chapter rules
* `sheets`: The LaTeX source for the character sheet
* `appendix/templates`: Jinja2 templates for the appendix documents
* `appendix/json`: JSON files with the game data from the website, fetched with the build script
* `appendix/latex`: The rendered appendix documents

### Building the documents

#### Requirements

To build the documents, you need to install the following:

* Python 3
* uv

#### Installing dependencies

To install the project dependencies, run `uv sync` in the project root directory.

#### Running ./build

To build the documents, the `build` script is invoked.

```shell
usage: build [-h] [-i IDS] [-d] [-o] [-l LANGUAGES] [-m MEDIA] [-k] [-u] [-a] [-c] [-p]

Build the project

options:
  -h, --help            show this help message and exit
  -i IDS, --ids IDS     IDs to build (['phasesix nexus tirakan'])
  -d, --debug           Debug mode
  -o, --publish         Upload existing PDFs from output without building
  -l LANGUAGES, --languages LANGUAGES
                        Languages to build (['de en'])
  -m MEDIA, --media MEDIA
                        Media to build (['online print'])
  -k, --keep-logs       Keep LaTeX logs
  -u, --update-appendix
                        Update appendix data
  -a, --appendix        Rebuild appendix files
  -c, --character-sheets-only
                        Only build character sheets
  -p, --preview         Open generated files in firefox
```
#### Variants, Languages and WorldBooks

The documents are organized in media variants, languages and world books. Variants are `print` and `online`. The online PDF lacks varying page numbers (left and right pages), chapters do not always start on the right page (this would lead to blank pages in the PDF) and pages do not have altering page margins.

The media variant is selected with the `-m` option.

```shell
$ uv run ./build -m print
```

The books support the languages `de` and `en`. The language is selected with the `-l` option.

```shell
$ uv run ./build -l de
```

The world books are `phasesix`, `nexus` and `tirakan`. Each book has its own wording, images and examples.

The world book is selected with the `-i` option.

```shell
$ uv run ./build -i nexus
```

#### Appendix-related options

The data for the appendix documents is fetched from the website `phasesix.org`. The data is updated with the `-u` option. To update the data, a phasesix API key is required. The build parameter `-a` determines whether the appendix files are rebuilt.

Both options are not required to build the documents, there are ready-to-use appendix files in the `appendix/latex` directory.

```shell
$ echo "API_KEY=my_api_key" > .env
$ uv run ./build -u
```

#### Uploading existing PDFs

The publish option uploads existing PDFs from the `output` directory. It does not
run LaTeX or create new PDFs.

```shell
$ uv run ./build --publish -i phasesix -l de -m online
```
