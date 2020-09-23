# Jupyter Notebooks (.ipynb)

Los ficheros Jupyter Notebooks (.ipynb) también pueden añadirse a nuestro libro, 
permitiendo la visualización y ejecución de bloques de código y sus outputs. 

## Celdas markdown

Permiten insertar imágenes, video, código HTML, etc. Ejemplo, esta imagen:

![](https://myst-parser.readthedocs.io/en/latest/_static/logo.png)

También podemos insertar $add_{math}$ y

$$
math^{blocks}
$$

o también

$$
\begin{aligned}
\mbox{mean} la_{tex} \\ \\
math blocks
\end{aligned}
$$

## Celdas MyST markdown

Las celdas MyST markdown funcionan en Jupyter Notebooks de modo similar. Para más información sobre MyST markdown, ver
[the MyST guide in Jupyter Book](https://jupyterbook.org/content/myst.html),
y [the MyST markdown documentation](https://myst-parser.readthedocs.io/en/latest/).

## Celdas de código y outputs

Jupyter Book permite la visualización de los bloques de código y outputs de los ficheros .ipynb.
Por ejemplo, esta es una muestra de código que utiliza Matplotlib:

from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);

Las posibilidades son muy diversas e incluyen el uso de outputs que permiten la interactividad en la lectura del libro
Para más información, ver [the Jupyter Book documentation](https://jupyterbook.org)