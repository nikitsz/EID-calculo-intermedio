# Grupo 11: Punto medio y punto interior

Proyecto de animación matemática con **Manim Community** para la Evaluación Integrada de Desempeño (EID), 2026.

## Identificación

- **Asignatura:** CÁLCULO INTERMEDIO — MATE 1134.
- **Sección:** 1.
- **Grupo:** 11 (G11).
- **Tema:** Punto medio y punto interior.
- **Pregunta central:** ¿Por qué el punto muestra no tiene que ser necesariamente un extremo ni el punto medio?
- **Repositorio:** https://github.com/nikitsz/EID-calculo-intermedio

| Integrante | GitHub | Responsabilidad principal y aportes |
| --- | --- | --- |
| DIEGO ANDRÉS VASQUEZ CONTRERAS | [@Clekz](https://github.com/Clekz) | Creación del README y edición del video |
| LUCAS ANDRÉS VILLEGAS ESCOBAR | [@LucsAndrs](https://github.com/LucsAndrs) | Explicación de la matemática |
| NICOLAS EFRAIN CALDERON PAINEVILO | [@nikitsz](https://github.com/nikitsz) | Creación del código |

Todos los integrantes deben comprender el proyecto completo y participar con su propia voz en una explicación matemática sustantiva.

## Objetivo

Mostrar que en cada subintervalo puede elegirse cualquier punto muestra $x_i^{\ast}\in[x_{i-1},x_i]$. La visualización compara el punto medio, los extremos y otro punto interior dentro de un mismo subintervalo, y explica cómo la elección determina la altura $f(x_i^{\ast})$ del rectángulo correspondiente.

## Fundamento y respuesta a la pregunta central

Para una partición uniforme de $[a,b]$ en $n$ subintervalos:

$$
\Delta x=\frac{b-a}{n},\qquad S_n=\sum_{i=1}^{n}f(x_i^{\ast})\Delta x.
$$

La definición de suma de Riemann permite elegir cualquier $x_i^{\ast}\in[x_{i-1},x_i]$. Los extremos y el punto medio son criterios particulares de elección, no condiciones obligatorias. El punto medio también es un punto interior.

Podemos expresar todas estas elecciones como:

$$
x_i^{\ast}=x_{i-1}+\theta_i(x_i-x_{i-1}),\qquad 0\leq\theta_i\leq1.
$$

Los valores $\theta_i=0$, $1$ y $1/2$ corresponden al extremo izquierdo, al derecho y al punto medio. Otros valores entre 0 y 1 producen puntos interiores distintos del punto medio. La elección puede variar de un subintervalo a otro.

La base del rectángulo depende de la partición; su altura depende de la función evaluada en el punto elegido. Una elección válida no tiene que dar exactamente el área bajo la curva en ese tramo.

## Ejemplo y comparación visual

La función representada es:

$$
f(x)=-0.2x^2+1.5x+1,\qquad x\in[0,5].
$$

La demostración local mantiene fija la base $[1,2.5]$, de ancho $1.5$, y mueve el punto muestra:

| Elección | $x_i^{\ast}$ | Altura $f(x_i^{\ast})$ | Área del rectángulo $1.5f(x_i^{\ast})$ |
| --- | --- | --- | --- |
| Punto medio inicial | 1.75 | 3.0125 | 4.51875 |
| Extremo izquierdo | 1 | 2.3 | 3.45 |
| Extremo derecho | 2.5 | 3.5 | 5.25 |
| Otro punto interior | 1.3 | 2.612 | 3.918 |

El punto rojo representa $(x_i^{\ast},f(x_i^{\ast}))$ y la línea vertical discontinua conecta el punto muestra con la altura. Al moverlo cambia la altura y, en este ejemplo, el área del rectángulo; el ancho permanece fijo. La tabla complementa la explicación: sus valores no aparecen escritos en la animación original.

Este tramo es una demostración local independiente y no coincide con una celda de la partición inicial de seis rectángulos.

### Conexión con la integral

La función es continua y positiva en $[0,5]$. Cuando el tamaño de los subintervalos tiende a cero, las sumas de Riemann convergen al área bajo la curva, independientemente de las elecciones válidas de puntos muestra:

$$
\lim_{n\to\infty}S_n=\int_0^5f(x)\,dx=\frac{185}{12}\approx15.4167.
$$

Como comprobación, la primera partición animada usa seis rectángulos, ancho $5/6$ y extremos derechos:

$$
S_6=\sum_{i=1}^{6}f\left(\frac{5i}{6}\right)\frac56
=\frac{1765}{108}\approx16.3426.
$$

Estos valores no se muestran numéricamente en el código. Una animación con 40 rectángulos ilustra el refinamiento, pero no demuestra por sí sola el límite.

## Escenas

Las tres clases se encuentran en [src/eid_calculo_intermedio/escenas.py](src/eid_calculo_intermedio/escenas.py).

| Clase | Contenido |
| --- | --- |
| ExplicacionFormula | Explica la sumatoria, la altura y la base del rectángulo. |
| MovingFrameBox | Presenta la función cuadrática y resalta sus términos. |
| Function | Grafica la función, delimita el intervalo, muestra seis rectángulos derechos, compara puntos muestra en una base fija y termina con particiones de 5, 15 y 40 rectángulos. |

En las particiones finales no se fija explícitamente el criterio de muestreo; se usa el valor predeterminado de la versión instalada de Manim.

## Requisitos y versiones

La configuración del repositorio en pyproject.toml declara:

| Componente | Configuración |
| --- | --- |
| Python | >=3.14 |
| Manim Community | >=0.22.0 |
| Gestor del proyecto | uv; dependencias resueltas en uv.lock |
| Construcción del paquete | uv_build >=0.12.5,<0.13.0 |
| NumPy | Importado por las escenas; no está declarado como dependencia directa en pyproject.toml |
| LaTeX | Necesario para las expresiones MathTex |

Los rangos declarados corresponden a la configuración del proyecto. Las versiones instaladas pueden consultarse con:

~~~bash
uv run python --version
uv run python -m manim --version
uv run python -c "import numpy; print(numpy.__version__)"
~~~

## Instalación y ejecución

Con Git, uv y las herramientas externas necesarias para Manim y LaTeX instalados:

~~~bash
git clone https://github.com/nikitsz/EID-calculo-intermedio.git
cd EID-calculo-intermedio
uv sync --locked
~~~

Desde la raíz del repositorio, renderizar vistas previas:

~~~bash
uv run python -m manim -pql src/eid_calculo_intermedio/escenas.py ExplicacionFormula
uv run python -m manim -pql src/eid_calculo_intermedio/escenas.py MovingFrameBox
uv run python -m manim -pql src/eid_calculo_intermedio/escenas.py Function
~~~

Para renderizar las tres escenas en calidad alta:

~~~bash
uv run python -m manim -qh src/eid_calculo_intermedio/escenas.py ExplicacionFormula MovingFrameBox Function
~~~

-p abre el resultado, -ql selecciona calidad baja y -qh calidad alta. Manim guarda los videos en media/videos/, con subcarpetas según el archivo y la calidad.

Cada escena genera un clip independiente. El montaje final y la narración se realizan mediante un editor de video.

## Estructura del repositorio

~~~text
.
├── README.md
├── .python-version
├── pyproject.toml
├── uv.lock
└── src/
    └── eid_calculo_intermedio/
        ├── README.md
        ├── __init__.py
        └── escenas.py
~~~

Este README principal documenta el proyecto.

## Referencias

1. **Manim Community Developers.** Manim Community Documentation. https://docs.manim.community/
2. **Pauta EID:** Higueras, N.; Oyarzo, F.; Matus, V. Evaluación Integrada de Desempeño: Introducción a la integral con Manim Community. Versión 2026. Documento del curso.

## Declaración de uso de inteligencia artificial

Se utilizó **Codex de OpenAI** para redactar y actualizar este README a partir del código, la pauta EID y los datos del grupo. La asistencia comprendió organización, descripción de escenas, explicación matemática e instrucciones de ejecución.

La revisión documental incluyó la lectura del código y la configuración del repositorio. No se renderizaron las escenas durante la elaboración del README.

