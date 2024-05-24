# Configuración

Jupyter Book utiliza un fichero de configuración que permite incluir numerosas funciones para personalizar los libros y crear experiencias interactivas con multitud de opciones.

El fichero de configuración se llama `_config.yml` y se crea al hacer `jupyter-book create` o bien, en el caso de este libro ejemplo, se copia junto con todos los demás contenidos del libro al hacer `git clone` como se explica en el capítulo correspondiente ([ver Mi primer libro](https://jero2760.github.io/jupyter-book-ejemplo/docs/chapter1/primerlibro.html)).

Se trata de un fichero clave, ya que controla tanto la visualización como la funcionalidad del libro. 

Este es el fichero `_config.yml` del libro ejemplo:
```bash
# Book settings
# Learn more at https://jupyterbook.org/customize/config.html

title: ¿Cómo crear un libro interactivo con Jupyter Book?
author: Publiconsulting Media
logo: logo.png

# Force re-execution of notebooks on each build.
# See https://jupyterbook.org/content/execute.html
execute:
  execute_notebooks: cache
  stderr_output: "remove"
  allow_errors: true
  timeout: 120

exclude_patterns: [file-types/include-rst.rst]

# Bibliography settings
bibtex_bibfiles:
    - docs/chapter2/references.bib

# Information about where the book exists on the web
repository:
  url: https://github.com/Jero2760/jupyter-book-ejemplo
  branch: master
  path_to_book: "docs"

launch_buttons:
  notebook_interface: "classic" # The interface interactive links will activate ["classic", "jupyterlab"]
  binderhub_url: "https://mybinder.org"
  colab_url: "https://colab.research.google.com"
  thebe: true

# Add GitHub buttons to your book
# See https://jupyterbook.org/customize/config.html#add-a-link-to-your-repository
html:
  google_analytics_id: UA-52617120-7
  home_page_in_navbar: false
  use_edit_page_button: true
  use_repository_button: true
  use_issues_button: true
  baseurl: https://publiconsulting.com/
  analytics:
    google_analytics_id = ''
  comments:
    hypothesis: true

parse:
  myst_substitutions:
      sub3: My _global_ value!
  myst_enable_extensions:  # default extensions to enable in the myst parser. See https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html
    - amsmath
    - colon_fence
    - deflist
    - dollarmath
    - html_admonition
    - html_image
    - linkify
    - replacements
    - smartquotes
    - substitution

# Define the name of the latex output file for PDF builds
latex:
  latex_engine: xelatex
  latex_documents:
    targetname: book.tex

sphinx:
  recursive_update: true
  config:
    bibtex_reference_style: author_year  # or label, super, \supercite
    # unknown_mime_type - application/vnd.plotly.v1+json and application/vnd.bokehjs_load.v0+json
    # domains - sphinx_proof.domain::prf needs to have `resolve_any_xref` method
    # mime_priority - latex priority not set in myst_nb for text/html, application/javascript
    suppress_warnings: ["mystnb.unknown_mime_type", "myst.domains", "mystnb.mime_priority"]
    copybutton_prompt_text: "$"
    nb_execution_show_tb: True
    nb_execution_timeout: 120
#    html_extra_path:
#      - images/badge.svg
    intersphinx_mapping:
      ebp:
        - "https://executablebooks.org/en/latest/"
        - null
      myst-parser:
        - "https://myst-parser.readthedocs.io/en/latest/"
        - null
      myst-nb:
        - "https://myst-nb.readthedocs.io/en/latest/"
        - null
      sphinx:
        - "https://www.sphinx-doc.org/en/master"
        - null
      nbformat:
        - "https://nbformat.readthedocs.io/en/latest"
        - null
      sd:
        - https://sphinx-design.readthedocs.io/en/latest
        - null
    language: en
    latex_elements:
        preamble: |
          \newcommand\N{\mathbb{N}}
          \newcommand\floor[1]{\lfloor#1\rfloor}
          \newcommand{\bmat}{\left[\begin{array}}
          \newcommand{\emat}{\end{array}\right]}
    # TODO: #917 this path will be the default in sphinx v4
    # mathjax_path: https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js
    # However, it is incompatible with the mathjax config below for macros
    mathjax3_config:
      tex:
        macros:
          "N": "\\mathbb{N}"
          "floor": ["\\lfloor#1\\rfloor", 1]
          "bmat": ["\\left[\\begin{array}"]
          "emat": ["\\end{array}\\right]"]
    nb_custom_formats:
      .Rmd:
        - jupytext.reads
        - fmt: Rmd
#    rediraffe_branch: 'master'
#    rediraffe_redirects:
#      content-types/index.md: file-types/index.md
#      content-types/markdown.md: file-types/markdown.md
#      content-types/notebooks.ipynb: file-types/notebooks.ipynb
#      content-types/myst-notebooks.md: file-types/myst-notebooks.md
#      content-types/jupytext.md: file-types/jupytext.Rmd
#      content-types/restructuredtext.md: file-types/restructuredtext.md
#      customize/toc.md: structure/toc.md
    sd_fontawesome_latex: True

    html_theme_options:
      navigation_with_keys: false

  extra_extensions:
    - sphinx_click.ext
    - sphinx_inline_tabs
#    - sphinxext.rediraffe
    - sphinx_proof
    - sphinx_examples

```
Algunos comentarios importantes:

- El path al fichero que contiene la bibliografía debe especificarse de esta manera: 

>bibtex_bibfiles:
>    - docs/chapter2/references.bib


Para entender esta configuración [ver la documentación](https://jupyterbook.org/en/stable/customize/config.html)