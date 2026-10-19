# Grupo 11: Punto medio y punto interior

Proyecto de animación matemática con **Manim Community** para la Evaluación Integrada de Desempeño (EID), 2026.

## Identificación

- **Asignatura:** CÁLCULO INTERMEDIO — MATE 1134.
- **Sección:** 1.
- **Grupo:** 11 (G11).
- **Tema:** Punto medio y punto interior.
- **Pregunta central:** ¿El punto muestra $x_i^{\ast}$ debe ser el punto medio o puede ser cualquier punto de $[x_{i-1},x_i]$, incluidos los extremos, para calcular la suma de Riemann finita $S_n$?
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

La conclusión conecta las sumas con la integral: como $f$ es continua en $[0,5]$, al tomar $\Delta x=5/n\to0$ se tiene $\lim_{n\to\infty}S_n=\int_0^5f(x)\,dx=185/12\approx15.4167$, para cualquier elección de puntos muestra en los intervalos cerrados. La portada y la conclusión muestran la pregunta con notación matemática, e incluyen explícitamente los extremos como opciones válidas. El montaje actualizado está en `output/videos/Videofinal_corregido.mp4` (ruta desde la raíz del proyecto).

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

El punto rojo representa $(x_i^{\ast},f(x_i^{\ast}))$ y la línea vertical discontinua conecta el punto muestra con la altura. En el zoom, las etiquetas $x_{i-1}$ y $x_i$ señalan los extremos, y $x_i^{\ast}$ sigue la proyección del punto rojo sobre el eje X. Al moverlo cambia la altura y, en este ejemplo, el área del rectángulo; el ancho permanece fijo. La tabla complementa la explicación: sus valores no aparecen escritos en la animación original.

Este tramo es una demostración local independiente y no coincide con una celda de la partición inicial de cinco rectángulos.

### Comparación de sumas finitas

Para un número fijo de subintervalos, la elección del punto muestra puede cambiar el valor de $S_n$. En la primera partición animada se usan cinco rectángulos, ancho $1$ y extremos derechos:

$$
S_5=\sum_{i=1}^{5}f(i)=16.5.
$$

La escena `EjemploNumerico` compara las sumas con $n=5,15,40$ usando extremos izquierdos, puntos medios y puntos interiores $x_i^{\ast}=x_{i-1}+\Delta x/3$. La escena `Function` termina mostrando particiones finitas de 5, 15 y 40 rectángulos.

## Escenas

Las escenas se encuentran en [escenas.py](escenas.py).

| Clase | Contenido |
| --- | --- |
| ExplicacionFormula | Explica la sumatoria, la altura y la base del rectángulo. |
| Portada | Presenta al grupo y la pregunta sobre la suma finita. |
| Teoria | Explica la partición y las opciones de punto muestra. |
| EjemploNumerico | Presenta la función y compara valores de sumas finitas. |
| Conclusion | Responde con el intervalo cerrado y conecta el límite de S_n con la integral definida. |
| Creditos | Muestra integrantes, referencias y herramientas. |
| Function | Grafica la función, delimita el intervalo, muestra cinco rectángulos derechos, compara puntos muestra en una base fija y termina con particiones de 5, 15 y 40 rectángulos. |

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
uv run python -m manim -pql src/eid_calculo_intermedio/escenas.py Portada Teoria EjemploNumerico Conclusion Creditos
uv run python -m manim -pql src/eid_calculo_intermedio/escenas.py Function
~~~

Para renderizar todas las escenas en calidad alta:

~~~bash
uv run python -m manim -qh src/eid_calculo_intermedio/escenas.py Portada Teoria ExplicacionFormula EjemploNumerico Function Conclusion Creditos
~~~

-p abre el resultado, -ql selecciona calidad baja y -qh calidad alta. Manim guarda los videos en media/videos/, con subcarpetas según el archivo y la calidad.

Cada escena genera un clip independiente. El montaje final y la narración se realizan mediante un editor de video.

## Videos generados

Los siete clips completos están disponibles en alta calidad (1920 × 1080, 60 fps). Cada escena es un archivo independiente, listo para descargar y montar con la narración.

- [Portada.mp4](../../media/videos/escenas/1080p60/Portada.mp4)
- [Teoria.mp4](../../media/videos/escenas/1080p60/Teoria.mp4)
- [ExplicacionFormula.mp4](../../media/videos/escenas/1080p60/ExplicacionFormula.mp4)
- [EjemploNumerico.mp4](../../media/videos/escenas/1080p60/EjemploNumerico.mp4)
- [Function.mp4](../../media/videos/escenas/1080p60/Function.mp4)
- [Conclusion.mp4](../../media/videos/escenas/1080p60/Conclusion.mp4)
- [Creditos.mp4](../../media/videos/escenas/1080p60/Creditos.mp4)

Los fragmentos temporales y las vistas previas de baja calidad se conservan localmente.

## Estructura del repositorio

~~~text
.
├── .python-version
├── pyproject.toml
├── uv.lock
└── src/
    └── eid_calculo_intermedio/
        ├── README.md
        ├── __init__.py
        └── escenas.py
~~~

Este README documenta el proyecto desde la carpeta de las escenas.

## Referencias

1. **Manim Community Developers.** Manim Community Documentation. https://docs.manim.community/
2. **Pauta EID:** Higueras, N.; Oyarzo, F.; Matus, V. Evaluación Integrada de Desempeño: Introducción a la integral con Manim Community. Versión 2026. Documento del curso.

## Declaración de uso de inteligencia artificial

Se utilizó **Codex de OpenAI** para redactar y actualizar este README a partir del código, la pauta EID y los datos del grupo. La asistencia comprendió organización, descripción de escenas, explicación matemática e instrucciones de ejecución.

La validación incluyó el renderizado de las siete escenas con Manim Community 0.22.0 y MiKTeX, en calidad de vista previa (480p, 15 fps). Se revisaron visualmente las fórmulas y el zoom, comprobando el punto rojo sobre la curva y las etiquetas de los extremos y del punto muestra.

