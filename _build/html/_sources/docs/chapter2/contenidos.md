# Tipos de contenidos

Jupyter Book admite muchos tipos de archivos para incluir en un libro. En general, estos son los tipos de contenido soportados por Jupyter Book:

- [Archivos Markdown](https://jupyterbook.org/en/stable/file-types/markdown.html): archivos de texto escritos en CommonMark o en MyST Markdown.

- [Jupyter Notebooks](https://jupyterbook.org/en/stable/file-types/notebooks.html): también conocidos como archivos .ipynb. Estos archivos pueden contener celdas Markdown con MyST Markdown. Un cuaderno Jupyter puede utilizar cualquier núcleo de programa que implemente el protocolo de mensajería Jupyter para ejecutar código. Hay kernels disponibles para Python, Julia, Ruby, Haskell y muchos otros lenguajes.

- [Cuadernos MyST Markdown](https://jupyterbook.org/en/stable/file-types/myst-notebooks.html): se trata de archivos Markdown (terminados en .md) que se convertirán en un cuaderno y se ejecutarán.

- [reStructuredText](https://jupyterbook.org/en/stable/file-types/restructuredtext.html): archivos de texto utilizados por el motor de documentación [Sphinx](https://www.writethedocs.org/guide/tools/sphinx/) (que es utilizado por Jupyter Book). Se recomienda utilizar MyST Markdown en su lugar.

- [Formatos de cuaderno personalizados](https://jupyterbook.org/en/stable/file-types/jupytext.html#file-types-custom): cualquier otro tipo de archivo puede ser auto-convertido antes de su ejecución asignándole una función Python personalizada, por ejemplo las proporcionadas por la herramienta de conversión Jupytext.

Para más información, ver la 
[documentación sobre tipos de contenido](https://jupyterbook.org/en/stable/file-types/index.html).

Existen diversos modos de escribir contenido en Jupyter Book. En los siguientes apartados de este capítulo se presentan algunas maneras de hacerlo, tanto en ficheros Jupyter Notebooks (.ipynb) como en ficheros markdown (.md) y se explica cómo añadir un fichero ipynb al libro.

