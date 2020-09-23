# ¿Cómo crear libros interactivos con Jupyter Book?

Con las herramientas de Jupyter, podemos crear libros interactivos que combinan texto, HTML y código de programación que puede ser ejecutado y modificado a voluntad.

A continuación vamos a ver un ejemplo de un libro de programación interactivo construido con Jupyter Book. 

## Jupyter Book

Jupyter Book es una herramienta open-source para crear libros y documentos PDF de calidad, con contenidos interactivos de código fuente de programación informática.

Jupyter Book permite a los usuarios

* escribir contenidos en [ficheros markdown (.md)](https://myst-parser.readthedocs.io/en/latest/) y [Jupyter Notebooks (.ipynb)](https://jupyter.org/),
* incluir elementos de programación (ej. código de programación) en ambos tipos, markdown y notebooks,
* incluir referencias bibliográficas y ecuaciones matemáticas, y
* usar un comando para ejecutar código embebido, [cache](https://jupyter-cache.readthedocs.io/en/latest/) el resultado y, finalmente,
* convertir el contenido de los ficheros markdown y notebooks en:
    * un libro interactivo para verlo en un browser (web-based interactive book) y
    * una publicación PDF de calidad.

Algunas de las funcionalidades principales de Jupyter Book son las siguientes:

{fa}`check,text-success mr-1` [Escribir contenidos en Markdown](https://jupyterbook.org/file-types/markdown)
: El contenido puede estar en Jupyter markdown, o bien en una versión de markdown extendido con [funciones de publicación avanzada](https://jupyterbook.org/content/myst).
Por ejemplo, pueden incluirse fácilmente contenidos en formato editorial como [referencias bibliográficas](https://jupyterbook.org/content/citations), [ecuaciones matemáticas](https://jupyterbook.org/content/math) y [gráficos](https://jupyterbook.org/content/figures).

{fa}`check,text-success mr-1` [Añadir código fuente directamente como ficheros Jupyter Notebooks](https://jupyterbook.org/file-types/notebooks)
: Esto permite incluir tanto el código como el resultado (output) de la ejecución directamente en el libro. Del mismo modo, también pueden escribirse notebooks [enteramente en markdown](https://jupyterbook.org/file-types/myst-notebooks) para ejecutar cuando se genera el libro con el comando 'build' como veremos más adelante.

{fa}`check,text-success mr-1` [Ejecutar y guardar en memoria cache el contenido del libro](https://jupyterbook.org/content/execute)
: Para ficheros Notebooks`.ipynb`, permite ejecutar código e insertar los últimos outputs.
  Esto permite además, {ref}`guardar en cache y re-utilizar<execute/cache>` los outputs posteriormente.

{fa}`check,text-success mr-1` [Insertar los outputs en el libro](https://jupyterbook.org/content:code-outputs)
: Se pueden insertar outputs a medida que se genera la documentación y añadirlos in-line con el resto de la página.

{fa}`check,text-success mr-1` [Añadir interactividad al libro](https://jupyterbook.org/interactive/launchbuttons)
: Por ejemplo, se puede [alternar la visibilidad de una celda](https://jupyterbook.org/interactive/hiding), incluir [outputs interactivos](https://jupyterbook.org/interactive/interactive) desde Jupyter y ejecutar el código [conectando con servicios online](https://jupyterbook.org/interactive/launchbuttons) como Binder, Google Colab y Deepnote.

{fa}`check,text-success mr-1` [Generar libros en HTML, PDF y otros formatos](https://jupyterbook.org/start/build)
: Esto incluye single- y multi-page websites, así como [PDF](https://jupyterbook.org/advanced/pdf).

{fa}`check,text-success mr-1` [Un libro se genera con un simple comando](https://jupyterbook.org/reference/cli)
: Por ejemplo, `jupyter-book build mybook/`

## Colabora

:::{admonition,tip} ¡Colabora con Jupyter Book!

Jupyter Book es una open community que agradece el feedback, input y las muestras de interés.

[Abir una cuestión (issue)](https://github.com/executablebooks/jupyter-book/issues/new/choose)
: para proporcionar feedback y nuevas ideas o comunicar problemas.

{ref}`Votar por nuevas funcionalidades <ebp:feature-note>`
: añadiendo 👍 a las cuestiones (issues) que deseas ver resueltas.

[Contribuir a Jupyter Book](https://jupyterbook.org/contribute/intro.md)
: siguiendo nuestra guía de participación e identificando una cuestión (issue) para trabajar en su resolución. Ver {ref}`la tabla de votación de funcionalidades <ebp:feature-note>` como ejemplo.

[En español puedes contactar con Publiconsulting Media](https://www.publiconsulting.com/about.html)
: para comentarios e ideas en español.

:::

## Agradecimientos

Jupyter Book cuenta con el soporte de una [comunidad abierta](https://github.com/executablebooks/jupyter-book/graphs/contributors), muchos de cuyos integrantes han participado en [the Jupyter community](https://jupyter.org/community).

Jupyter Book y muchas de las herramientas que utiliza están promovidas por [the Executable Book Project](https://executablebooks.org), que a su vez cuenta con el apoyo de [the Alfred P. Sloan foundation](https://sloan.org/grant-detail/9231).

