# Grupo 11: Punto medio y punto interior

Proyecto de animación matemática con **Manim Community** para la Evaluación Integrada de Desempeño (EID), 2026.

**Estado del montaje al 18 de octubre de 2026:** video de **6 minutos exactos**, en **1920 × 1080 y 60 fps**, con las narraciones de Diego y Lucas sincronizadas. Falta incorporar la voz de Nicolás en el tramo **01:25–03:25**.

## Identificación

- **Asignatura:** CÁLCULO INTERMEDIO — MATE 1134.
- **Sección:** 1.
- **Grupo:** 11 (G11).
- **Tema:** Punto medio y punto interior.
- **Pregunta central:** ¿El punto muestra $x_i^{\ast}$ debe ser obligatoriamente el punto medio o puede ser cualquier punto interior de $[x_{i-1},x_i]$ para calcular la suma de Riemann finita $S_n$?
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

El punto rojo representa $(x_i^{\ast},f(x_i^{\ast}))$ y la línea vertical discontinua conecta el punto muestra con la altura. En el zoom, el eje X permanece visible, las etiquetas $x_{i-1}$ y $x_i$ señalan los extremos, y $x_i^{\ast}$ sigue la proyección del punto rojo sobre el eje X. Al moverlo cambia la altura y, en este ejemplo, el área del rectángulo; el ancho permanece fijo. La tabla complementa la explicación: sus valores no aparecen escritos en la animación original.

Este tramo es una demostración local independiente y no coincide con una celda de la partición inicial de cinco rectángulos.

### Comparación de sumas finitas

Para un número fijo de subintervalos, la elección del punto muestra puede cambiar el valor de $S_n$. En la primera partición animada se usan cinco rectángulos, ancho $1$ y extremos derechos:

$$
S_5=\sum_{i=1}^{5}f(i)=16.5.
$$

La escena `EjemploNumerico` compara las sumas con $n=5,15,40$ usando extremos izquierdos, puntos medios y puntos interiores $x_i^{\ast}=x_{i-1}+\Delta x/3$. La escena `Function` termina mostrando particiones finitas de 5, 15 y 40 rectángulos.

## Escenas

Las escenas se encuentran en [escenas.py](src/eid_calculo_intermedio/escenas.py). La tabla sigue el orden y los tiempos del montaje editado de seis minutos; las duraciones de los clips originales son distintas.

| Clase | Tiempo en el montaje | Duración | Contenido |
| --- | --- | --- | --- |
| Portada | 00:00–00:24 | 24 s | Presenta al grupo y la pregunta sobre la suma finita. |
| Teoria | 00:24–00:49 | 25 s | Explica la partición y las opciones de punto muestra. |
| ExplicacionFormula | 00:49–01:25 | 36 s | Explica la sumatoria, la altura y la base del rectángulo. |
| EjemploNumerico | 01:25–02:15 | 50 s | Presenta la función y compara valores de sumas finitas. |
| Function | 02:15–04:44 | 149 s | Grafica la función, delimita el intervalo, muestra cinco rectángulos derechos, compara puntos muestra en una base fija y termina con particiones de 5, 15 y 40 rectángulos. |
| Conclusion | 04:44–05:30 | 46 s | Responde la pregunta con la fórmula de S_n. |
| Creditos | 05:30–06:00 | 30 s | Muestra integrantes, referencias y herramientas. |

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
| FFmpeg y ffprobe | Utilizados en la edición para montar las escenas, tratar y sincronizar el audio y verificar el archivo exportado |

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

Cada escena genera un clip independiente. La versión de seis minutos se obtiene mediante una edición posterior con FFmpeg; ejecutar únicamente Manim no genera ese montaje ni incorpora las voces.

## Videos generados

### Montaje editado de seis minutos

La versión local más reciente es:

~~~text
output/videos/Grupo_11_Suma_Riemann_6_minutos_final_Diego_actualizado.mp4
~~~

Conserva los contenidos de las siete escenas. La duración se amplió mediante animaciones más lentas y pausas sobre la imagen. Las voces se dividieron por frases y se colocaron con silencios para acompañar las fórmulas, los movimientos del punto muestra y los créditos. El último cambio reemplazó la narración final de Diego por su nueva grabación.

Se aplicaron ajustes moderados de ruido y volumen a las grabaciones. El montaje conserva la imagen en 1080p y 60 fps, con audio AAC estéreo a 48 kHz. La duración de 360 segundos y la decodificación completa de imagen y sonido se verificaron después de la exportación. Estas ediciones se realizaron fuera del código base de las escenas.

El archivo editado y los materiales de narración se conservan localmente; todavía no están versionados en Git. Su presencia en este README no significa que puedan descargarse desde GitHub. El MP4 anterior `output/videos/Grupo_11_Suma_Riemann.mp4` corresponde al montaje breve original, no a la edición actual de seis minutos.

### Reparto y estado de las narraciones

El guion asigna **120 segundos de video a cada integrante**, incluidas las pausas. La duración efectiva de voz puede ser menor.

| Integrante | Tramos asignados | Contenido | Estado |
| --- | --- | --- | --- |
| Diego | 00:00–00:49; 03:25–04:06; 05:30–06:00 | Portada, teoría, movimiento del punto en el zoom y créditos | Audios incorporados y sincronizados; final reemplazado por la nueva grabación |
| Lucas | 00:49–01:25; 04:06–05:30 | Fórmula, particiones finales y conclusión | Cinco grabaciones incorporadas, con cortes entre frases y pausas |
| Nicolás | 01:25–03:25 | Ejemplo numérico, gráfica y entrada al zoom | Narración pendiente; el contenido visual ya está incluido |

Las partes sin grabación permanecen sin narración. Para completar el montaje falta incorporar las voces de Nicolás y revisar la reproducción del video completo con los tres integrantes.

### Guion y material de estudio

Los siguientes materiales están disponibles en la copia local:

- `output/pdf/Guion_narracion_estudio_Grupo_11_6_minutos.pdf`: guía de narración con tiempos, reparto y notas de estudio.
- `docs/guion_audio_6min/Guion_estudio_narracion_6_minutos.md`: versión editable del guion, con pronunciación de símbolos y cálculos del zoom.
- `docs/guion_audio_6min/`: nueve archivos de texto con las partes para grabar; la escena gráfica está dividida entre las tres voces.
- `docs/PAUTA_REPASO_GRUPO_11.md`: repaso de la matemática y del funcionamiento del proyecto.

### Clips originales por escena

Los siete clips completos están disponibles en alta calidad (1920 × 1080, 60 fps). Son las animaciones independientes previas a la edición de duración y narración:

- [Portada.mp4](media/videos/escenas/1080p60/Portada.mp4)
- [Teoria.mp4](media/videos/escenas/1080p60/Teoria.mp4)
- [ExplicacionFormula.mp4](media/videos/escenas/1080p60/ExplicacionFormula.mp4)
- [EjemploNumerico.mp4](media/videos/escenas/1080p60/EjemploNumerico.mp4)
- [Function.mp4](media/videos/escenas/1080p60/Function.mp4)
- [Conclusion.mp4](media/videos/escenas/1080p60/Conclusion.mp4)
- [Creditos.mp4](media/videos/escenas/1080p60/Creditos.mp4)

Los fragmentos temporales y las vistas previas de baja calidad se conservan localmente.

## Estructura del repositorio

~~~text
.
├── .python-version
├── pyproject.toml
├── uv.lock
├── README.md
├── docs/                   # Guion y material de estudio local
├── audios/                 # Grabaciones disponibles para la edición
├── media/videos/escenas/    # Clips renderizados de Manim
├── output/
│   ├── pdf/                # Guías en PDF
│   └── videos/             # Montaje y archivos auxiliares de edición
└── src/
    └── eid_calculo_intermedio/
        ├── README.md
        ├── __init__.py
        └── escenas.py
~~~

Este README documenta el proyecto desde la raíz del repositorio. Parte del material de edición es local y no está incluido en GitHub.

## Referencias

1. **Manim Community Developers.** Manim Community Documentation. https://docs.manim.community/
2. **Pauta EID:** Higueras, N.; Oyarzo, F.; Matus, V. Evaluación Integrada de Desempeño: Introducción a la integral con Manim Community. Versión 2026. Documento del curso.
3. **Stewart, J. (2012).** Cálculo de una variable: Trascendentes tempranas. Referencia declarada en los créditos del video.
4. **Material de la asignatura.** Apuntes y material del curso de Cálculo Intermedio. Referencia declarada en los créditos del video.

## Declaración de uso de inteligencia artificial

Se utilizó **Codex de OpenAI** para redactar y actualizar este README a partir del código, la pauta EID y los datos del grupo. La asistencia comprendió organización, descripción de escenas, explicación matemática e instrucciones de ejecución. También se utilizó para preparar el guion y las guías de estudio, apoyar correcciones de la animación y realizar la edición con FFmpeg: ampliación de duración, tratamiento de audio, cortes, pausas y sincronización por frases. Se empleó reconocimiento de voz ejecutado localmente para ubicar las frases dentro de las grabaciones.

Las voces incorporadas son grabaciones de los integrantes; no se generaron voces sintéticas. Las ediciones de duración y narración se realizaron sin modificar el código base de las escenas. En los créditos también se declara el uso de asistencia de IA para la sintaxis de Manim y el guion.

La validación incluyó el renderizado de las siete escenas con Manim Community 0.22.0 y MiKTeX, tanto en vista previa (480p, 15 fps) como en alta calidad (1080p, 60 fps). Se revisaron visualmente las fórmulas y el zoom, comprobando el punto rojo sobre la curva, las etiquetas de los extremos y del punto muestra y la continuidad del eje X. Para el montaje actual se verificaron además la duración de seis minutos, los intervalos de narración, los niveles de audio y la decodificación completa del archivo exportado.

