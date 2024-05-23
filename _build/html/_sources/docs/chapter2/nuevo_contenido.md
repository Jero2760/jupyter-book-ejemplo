# Cómo añadir nuevo contenido a nuestro libro

En este ejemplo vamos a añadir un nuevo notebook a nuestro libro:

1. Incluir una nueva línea en el fichero _toc.yml con el nombre del nuevo notebook. En este caso lo llamamos mi_nuevo_notebook.ipynb y lo vamos a incluir en un nuevo capítulo del libro (chapter4). Así queda _toc.yml:
```bash
format: jb-book
root: docs/chapter0/intro
parts:
- caption: Inicio
  numbered: true
  chapters:
  - file: docs/chapter0/installation
- caption: Contenido
  numbered: true
  chapters:
  - file: docs/chapter1/primerlibro
  - file: docs/chapter2/contenidos
    sections:
    - file: docs/chapter2/markdown
    - file: docs/chapter2/notebooks
  - file: docs/chapter3/publish
  - file: docs/chapter4/mi_nuevo_notebook.ipynb
```

2. El siguiente paso es asegurarnos que el nuevo notebook se incorpora a la carpeta docs de la estructura del libro jupyter-book-ejemplo. Para ello se crea una carpeta llamada chapter4 y allí se incluye el fichero mi_nuevo_notebook.ipynb.

3. Luego se ejecuta:  jupyter-book build jupyter-book-ejemplo

4. Y ya está añadido el nuevo notebook al libro. Se puedo ver haciendo doble click en index.html (en la carpeta _build/html). En este caso se ha creado un nuevo capítulo cuyo título es la primera línea del notebook añadido.

Añadir un nuevo fichero .md se hace de forma similar. [Ver documentación](https://jupyterbook.org/en/stable/start/new-file.html)
