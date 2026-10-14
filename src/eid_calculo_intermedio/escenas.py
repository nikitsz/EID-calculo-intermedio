from manim import *
import numpy as np

class MovingFrameBox(Scene):

  def construct(self):
    text = MathTex(r"f(x) = -0.2 x^2 + 1.5 x + 1",
    substrings_to_isolate=["0.2", "1.5", "1"]
    )


    self.play(Write(text))

    framebox1 = SurroundingRectangle(text.get_part_by_tex("0.2"), buff=0.1)
    framebox2 = SurroundingRectangle(text.get_part_by_tex("1.5"), buff=0.1)
    framebox3 = SurroundingRectangle(text.get_part_by_tex("1"), buff=0.1)

    self.play(Create(framebox1))
    self.wait()
        
    self.play(ReplacementTransform(framebox1, framebox2))
    self.wait()
        
    self.play(ReplacementTransform(framebox2, framebox3))
    self.wait()

class SinAndCosFunctionPlot(Scene): # Puedes cambiar el nombre de la clase si lo prefieres
    def construct(self):
        # 1. Configuración de los ejes coordenados
        axes = Axes(
            x_range=[-10, 10.3, 1],
            y_range=[-4, 5, 1], # Corregido: sintaxis correcta para y_range [min, max, step]
            x_length=10,
            axis_config={"numbers_to_include": np.arange(-4, 5, 1),
            "color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-10, 11, 2),
                "numbers_with_elongated_ticks": np.arange(-10, 11, 2),
            },
            tips=False,
        )
        axes_labels = axes.get_axis_labels()

        # 2. Definición de la gráfica (Parábola)
        func_graph = axes.plot(
            lambda x: -0.2 * (x**2) + 1.5 * x + 1, 
            color=BLUE, 
            x_range=[-6, 11]
        )

        # 3. Etiqueta de la función
        func_label = axes.get_graph_label(func_graph, label="f(x)", x_val=2, direction=UP)

        # 4. Línea vertical en x = 5 (Cambiado TAU por un valor dentro del rango visible de la curva)
        

        # ==========================================================
        # SECUENCIA DE ANIMACIÓN 🎬
        # ==========================================================
        
        # 1. Dibuja los ejes y escribe los nombres (X e Y) simultáneamente
        self.play(Create(axes), Write(axes_labels), run_time=2)
        self.wait(0.5)

        # 2. Traza la gráfica de la función
        self.play(
            Create(func_graph), 
            run_time=2.5, 
            rate_func=linear
        )

        # 3. Aparece la etiqueta f(x)
        self.play(FadeIn(func_label))
        self.wait(0.5)

        # 4. Se traza la línea vertical amarilla

        # Mantiene el resultado final en pantalla por 2 segundos antes de terminar
        self.wait(10)
        x_value_1 = 5
        vert_line_5 = axes.get_vertical_line(axes.i2gp(x_value_1, func_graph), color=YELLOW)

        x_value_2 = 0
        vert_line_0 = axes.get_vertical_line(axes.i2gp(x_value_2, func_graph), color=YELLOW)

        intervalo = axes.get_graph_label(func_graph, label="[0, 5]", x_val=4, direction=DOWN)
        self.play(Write(intervalo), run_time=2)
        self.play(Create(vert_line_5), run_time=1)
        self.play(Create(vert_line_0), run_time=1)
        

        self.wait(2)
