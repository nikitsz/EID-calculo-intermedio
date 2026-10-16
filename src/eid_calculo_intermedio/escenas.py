from manim import *
import numpy as np

class ExplicacionFormula(Scene):
    def construct(self):
        formula = MathTex(
            r"S_n", r"=", r"\sum_{i=1}^{n}", r"f(x_i^*)", r"\Delta x"
        ).scale(1.3)

        self.play(Write(formula))
        self.wait(1)

        # Destacar la suma de rectángulos
        box_sum = SurroundingRectangle(formula[2], color=YELLOW)
        lbl_sum = Text("Suma de n rectángulos", font_size=24, color=YELLOW).next_to(box_sum, UP)
        self.play(Create(box_sum), Write(lbl_sum))
        self.wait(2)

        # Destacar la altura f(x_i*)
        box_height = SurroundingRectangle(formula[3], color=RED)
        lbl_height = Text("Altura (Punto muestra x_i*)", font_size=24, color=RED).next_to(box_height, UP, buff=0.5)
        self.play(ReplacementTransform(box_sum, box_height), ReplacementTransform(lbl_sum, lbl_height))
        self.wait(2)

        # Destacar el ancho Delta x
        box_dx = SurroundingRectangle(formula[4], color=BLUE)
        lbl_dx = Text("Ancho base (Δx)", font_size=24, color=BLUE).next_to(box_dx, UP)
        self.play(ReplacementTransform(box_height, box_dx), ReplacementTransform(lbl_height, lbl_dx))
        self.wait(2)

class MovingFrameBox(MovingCameraScene):

  def construct(self):
    text = MathTex(r"f(x) = -0.2 x^2 + 1.5 x + 1",
    substrings_to_isolate=["0.2 x^2", "1.5 x", "1"]
    )


    self.play(Write(text))

    framebox1 = SurroundingRectangle(text.get_part_by_tex("0.2 x^2"), buff=0.1)
    framebox2 = SurroundingRectangle(text.get_part_by_tex("1.5 x"), buff=0.1)
    framebox3 = SurroundingRectangle(text.get_part_by_tex("1"), buff=0.1)

    self.play(Create(framebox1))
    self.wait()
        
    self.play(ReplacementTransform(framebox1, framebox2))
    self.wait()
        
    self.play(ReplacementTransform(framebox2, framebox3))
    self.wait()

class Function(MovingCameraScene): 
    def get_rectangle_corners(self, x_min, x_max, height):
        return [
            (x_min, 0),
            (x_min, height),
            (x_max, height),
            (x_max, 0),
        ]
    
    def construct(self):
        # 1. Configuración de los ejes coordenados
        func = lambda x: -0.2 * (x**2) + 1.5 * x + 1
       
        axes = Axes(
            x_range=[-6, 10, 1],
            y_range=[-4, 5, 1], 
            x_length=10,
            axis_config={"numbers_to_include": np.arange(-4, 5, 1),
            "color": GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-6, 11, 2),
                "numbers_with_elongated_ticks": np.arange(-6, 11, 2),
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
        # SECUENCIA DE ANIMACIÓN 
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
        x_value_1 = 5
        vert_line_5 = axes.get_vertical_line(axes.i2gp(x_value_1, func_graph), color=YELLOW)

        x_value_2 = 0
        vert_line_0 = axes.get_vertical_line(axes.i2gp(x_value_2, func_graph), color=YELLOW)

        intervalo = MathTex(r"[0, 5]").next_to(axes.c2p(2.5, 0), DOWN)
        self.play(Create(vert_line_5), run_time=1)
        self.play(Create(vert_line_0), run_time=1)
        

        self.wait(2)

        riemann_rects = axes.get_riemann_rectangles(
            func_graph,
            x_range=[0, 5],
            dx=5/6,
            input_sample_type="right", # O "left", "center"
            stroke_width=1,
            stroke_color=WHITE,
            fill_opacity=0.3,
            color=TEAL
        )

        self.play(Create(riemann_rects), run_time=2)
        self.wait(3) # Pausa para explicar la partición global

        self.play(FadeOut(riemann_rects), run_time=1)
        
        punto_enfoque = axes.c2p(1.75, 1.2)

     # 2. Hacemos el acercamiento de cámara en 2.5 segundos
        self.play(
        self.camera.frame.animate.scale(0.45).move_to(punto_enfoque),
        run_time=2.5
     )

     # 3. Pausa para continuar hablando con el zoom puesto
        self.wait(5)

        x_min, x_max = 1.0, 2.5

        # Tramo acotado
        sub_func_graph = axes.plot(
            func, 
            x_range=[x_min, x_max], 
            color=YELLOW, # Cambiar color para destacar
            stroke_width=6
        )

        # Atenuamos la curva completa (20% de opacidad) y hacemos aparecer el tramo
        self.play(
            func_graph.animate.set_opacity(0.25),
            Create(sub_func_graph),
            run_time=1.5
        )
        self.wait(2)

        t = ValueTracker(1.75) # Punto medio inicial

        # Polígono redibujado según t.get_value()
        def get_rectangle():
            height = func(t.get_value())
            corners = self.get_rectangle_corners(x_min, x_max, height)
            polygon = Polygon(*[axes.c2p(*pt) for pt in corners])
            polygon.set_stroke(YELLOW_B, width=2)
            polygon.set_fill(TEAL, opacity=0.4)
            return polygon

        rectangle = always_redraw(get_rectangle)

        # Punto sobre la curva f(x_i*)
        dot = Dot(color=RED)
        dot.add_updater(lambda d: d.move_to(axes.c2p(t.get_value(), func(t.get_value()))))
        dot.set_z_index(10)

        # Proyección vertical
        dashed_line = always_redraw(
            lambda: DashedLine(
                axes.c2p(t.get_value(), 0),
                axes.c2p(t.get_value(), func(t.get_value())),
                color=RED
            )
        )

        # Aparece el rectángulo en pantalla
        self.add(rectangle, dot, dashed_line)
        self.wait(2)

        # DEMOSTRACIÓN DE LA PREGUNTA CENTRAL: Mover x_i*
        # 1. Extremo izquierdo (1.0)
        self.play(t.animate.set_value(1.0), run_time=2)
        self.wait(1)

        # 2. Extremo derecho (2.5)
        self.play(t.animate.set_value(2.5), run_time=2)
        self.wait(1)

        # 3. Punto interior arbitrario (1.3)
        self.play(t.animate.set_value(1.3), run_time=2)
        self.wait(3)
        self.play(FadeOut(rectangle, dot, dashed_line, sub_func_graph))
        # Camara vuelve a la vista completa
        self.play(
            self.camera.frame.animate.scale(1 / 0.45).move_to(axes.get_center()),
            func_graph.animate.set_opacity(1),
            run_time=2
        )
        self.wait(0.5)

        riemann_rects = axes.get_riemann_rectangles(
            func_graph, x_range=[0, 5], dx=5/5, fill_opacity=0.4, color=TEAL
        )
        self.play(Create(riemann_rects), run_time=1.5)

        for num_rects in [5, 15, 40]:
            new_rects = axes.get_riemann_rectangles(
                func_graph,
                x_range=[0, 5],
                dx=5/num_rects,
                fill_opacity=0.4,
                color=TEAL
            )
            self.play(Transform(riemann_rects, new_rects), run_time=1.5)
            self.wait(2)