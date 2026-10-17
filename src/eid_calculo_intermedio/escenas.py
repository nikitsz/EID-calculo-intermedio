from manim import *
import numpy as np

class Portada(Scene):
    def construct(self):
        # 1. CREACIÓN DE OBJETOS DE TEXTO
        titulo = Text("Punto Medio y Punto Interior", font_size=36, color=YELLOW)
        subtitulo = Text("MAT1134 - Cálculo Intermedio | Grupo 11", font_size=22, color=GRAY_A)
        integrantes = Text("Lucas Villegas - Diego Vásquez - Nicolás Calderón", font_size=18, color=WHITE)

        # Bloque de la Pregunta Central
        pregunta_hdr = Text("Pregunta Central:", font_size=20, color=YELLOW_B)
        pregunta = Text(
            "¿Es estrictamente necesario que el punto muestra x_i*\n"
            "sea el punto medio, o puede ser cualquier punto interior\n"
            "al tomar el límite cuando n → ∞?",
            font_size=18, color=WHITE
        )

        # 2. AGRUPACIÓN Y ORDENAMIENTO (LAYOUT)
        encabezado = VGroup(titulo, subtitulo, integrantes).arrange(DOWN, buff=0.3)
        bloque_pregunta = VGroup(pregunta_hdr, pregunta).arrange(DOWN, buff=0.2)

        # Agrupamos los dos bloques principales
        pantalla_completa = VGroup(encabezado, bloque_pregunta).arrange(DOWN, buff=0.7)

        # 3. SECUENCIA DE ANIMACIÓN
        self.play(Write(encabezado), run_time=2.5)
        self.wait(1)
        
        self.play(FadeIn(bloque_pregunta), run_time=2)
        self.wait(3)

class Teoria(Scene):
    def construct(self):
        # 1. TÍTULO UN POCO MÁS PEQUEÑO Y CON MARGEN
        titulo = Text("Teoría: Suma de Riemann y Punto Muestra", font_size=22, color=YELLOW).to_edge(UP, buff=0.4)

        # 2. SECCIONES CON FORMATEO MATEMÁTICO REAL
        t1 = Text("1. División del intervalo [a, b]:", font_size=16, color=BLUE)
        sub1 = MathTex(r"\text{Dividimos el dominio en } n \text{ subintervalos de ancho } \Delta x.", font_size=18)

        t2 = Text("2. Elección del punto muestra:", font_size=16, color=GREEN)
        sub2 = MathTex(r"\text{En cada } [x_{i-1}, x_i], \text{ elegimos } x_i^* \text{ para evaluar } f(x_i^*).", font_size=18)

        t3 = Text("3. Opciones habituales para } x_i^*:", font_size=16, color=ORANGE)
        op1 = MathTex(r"\bullet \text{ Extremo izquierdo: } x_i^* = x_{i-1}", font_size=17)
        op2 = MathTex(r"\bullet \text{ Extremo derecho: } x_i^* = x_i", font_size=17)
        op3 = MathTex(r"\bullet \text{ Punto medio: } x_i^* = \frac{x_{i-1} + x_i}{2}", font_size=17)
        op4 = MathTex(r"\bullet \text{ Punto interior arbitrario: } x_{i-1} < x_i^* < x_i", font_size=17)

        opciones = VGroup(op1, op2, op3, op4).arrange(DOWN, aligned_edge=LEFT, buff=0.12)

        # 3. AGRUPACIÓN Y ALINEACIÓN
        g1 = VGroup(t1, sub1).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        g2 = VGroup(t2, sub2).arrange(DOWN, aligned_edge=LEFT, buff=0.08)
        g3 = VGroup(t3, opciones).arrange(DOWN, aligned_edge=LEFT, buff=0.08)

        contenido = VGroup(g1, g2, g3).arrange(DOWN, aligned_edge=LEFT, buff=0.22)
        contenido.next_to(titulo, DOWN, buff=0.3)

        # 4. ANIMACIÓN
        self.play(Write(titulo))
        self.wait(0.3)
        self.play(FadeIn(g1))
        self.play(FadeIn(g2))
        self.play(FadeIn(g3))
        self.wait(3)
        
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

class EjemploNumerico(Scene):
    def construct(self):
        # 1. TÍTULO
        titulo = Text("Ejemplo Propio y Cálculo Algebraico", font_size=28, color=YELLOW).to_edge(UP)
        self.play(Write(titulo))
        self.wait(0.5)

        # 2. TU ANIMACIÓN DE LA FUNCIÓN (MovingFrameBox integrada)
        f_tex = MathTex(
            r"f(x) = ", r"-0.2 x^2", r" + ", r"1.5 x", r" + ", r"1", 
            r"\quad \text{en } [0, 5]",
            font_size=22
        )
        f_tex.next_to(titulo, DOWN, buff=0.4)

        self.play(Write(f_tex))

        # Recuadros para cada componente
        framebox1 = SurroundingRectangle(f_tex[1], color=YELLOW, buff=0.1)
        framebox2 = SurroundingRectangle(f_tex[3], color=YELLOW, buff=0.1)
        framebox3 = SurroundingRectangle(f_tex[5], color=YELLOW, buff=0.1)

        self.play(Create(framebox1))
        self.wait(0.5)
        self.play(ReplacementTransform(framebox1, framebox2))
        self.wait(0.5)
        self.play(ReplacementTransform(framebox2, framebox3))
        self.wait(0.5)
        self.play(FadeOut(framebox3))

        # 3. INTEGRAL Y ÁREA EXACTA
        area_exacta = MathTex(
            r"\text{Área exacta} = \int_0^5 f(x) \, dx = \frac{185}{12} \approx 15.4167",
            font_size=22, color=GREEN
        ).next_to(f_tex, DOWN, buff=0.3)

        self.play(Write(area_exacta))
        self.wait(1)

        # 4. TABLA COMPARATIVA
        hdr_tabla = MathTex(
            r"\text{Aproximaciones } S_n \text{ según la elección de } x_i^*:",
            font_size=18, color=WHITE
        )
        tabla = MobjectTable(
            [
                [Text("n", font_size=16, color=YELLOW), Text("Extremo Izq.", font_size=16), Text("Punto Medio", font_size=16), Text("Punto Interior", font_size=16)],
                [Text("5", font_size=16), Text("14.0000", font_size=16), Text("15.5000", font_size=16), Text("14.8333", font_size=16)],
                [Text("15", font_size=16), Text("14.9352", font_size=16), Text("15.4259", font_size=16), Text("15.2201", font_size=16)],
                [Text("40", font_size=16), Text("15.2344", font_size=16), Text("15.4180", font_size=16), Text("15.3418", font_size=16)],
                [Text("∞", font_size=16, color=GREEN), Text("15.4167", font_size=16, color=GREEN), Text("15.4167", font_size=16, color=GREEN), Text("15.4167", font_size=16, color=GREEN)]
            ],
            line_config={"stroke_width": 1}
        ).scale(0.8)

        bloque_inferior = VGroup(hdr_tabla, tabla).arrange(DOWN, buff=0.2)
        bloque_inferior.next_to(area_exacta, DOWN, buff=0.3)

        self.play(FadeIn(hdr_tabla), Create(tabla))
        self.wait(4)
        
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
        func_graph.set_fill(opacity=0)

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

        intervalo = MathTex(r"[0, 5]", color=YELLOW).next_to(axes.c2p(2.5, 0), DOWN, buff=0.75)
        self.play(Write(intervalo))
        self.play(Create(vert_line_5), run_time=1)
        self.play(Create(vert_line_0), run_time=1)
        

        self.wait(2)

        riemann_rects = axes.get_riemann_rectangles(
            func_graph,
            x_range=[0, 5],
            dx=5/5,
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
        func_graph.animate.set_stroke(opacity=0.25),
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
            func_graph.animate.set_stroke(opacity=1),
            run_time=2
        )
        self.wait(0.5)

        riemann_rects = axes.get_riemann_rectangles(
            func_graph, x_range=[0, 5], dx=5/5, fill_opacity=0.4, color=TEAL
        )
        self.play(Create(riemann_rects), run_time=1.5)

        for num_rects in [15, 40]:
            new_rects = axes.get_riemann_rectangles(
                func_graph,
                x_range=[0, 5],
                dx=5/num_rects,
                fill_opacity=0.4,
                color=TEAL
            )
            self.play(Transform(riemann_rects, new_rects), run_time=1.5)
            self.wait(2)
            
class Conclusion(Scene):
    def construct(self):
        # 1. TÍTULO
        titulo = Text("Conclusión del Proyecto", font_size=26, color=YELLOW).to_edge(UP, buff=0.3)

        # 2. REPETICIÓN DE LA PREGUNTA CENTRAL
        pregunta_hdr = Text("Pregunta Central:", font_size=18, color=YELLOW_B)
        pregunta_txt = Text(
            "\"¿Es estrictamente necesario que el punto muestra x_i* sea el punto medio,\n"
            "o puede ser cualquier punto interior al tomar el límite cuando n → ∞?\"",
            font_size=15, color=WHITE
        )
        bloque_pregunta = VGroup(pregunta_hdr, pregunta_txt).arrange(DOWN, buff=0.1)

        # 3. RESPUESTA FORMAL
        respuesta = Text("Respuesta: NO es estrictamente necesario.", font_size=18, color=GREEN)

        p1 = MathTex(
            r"\bullet \text{ Como } f(x) \text{ es continua en } [0, 5], \text{ el ancho } \Delta x = \frac{5-0}{n} \to 0 \text{ cuando } n \to \infty.",
            font_size=16
        )
        p2 = MathTex(
            r"\bullet \text{ Al volverse } \Delta x \text{ infinitamente pequeño, la elección de } x_i^* \text{ no altera el valor final}.",
            font_size=16
        )

        # 4. RESULTADO ENMARCADO
        formula_final = MathTex(
            r"\lim_{n \to \infty} \sum_{i=1}^{n} f(x_i^*) \Delta x = \int_0^5 f(x) \, dx = \frac{185}{12} \approx 15.4167",
            font_size=20
        )
        box = SurroundingRectangle(formula_final, color=YELLOW, buff=0.15)
        resultado = VGroup(box, formula_final)

        # 5. DISPOSICIÓN Y ANIMACIÓN
        cuerpo = VGroup(bloque_pregunta, respuesta, p1, p2, resultado).arrange(DOWN, buff=0.22)
        cuerpo.next_to(titulo, DOWN, buff=0.3)

        self.play(Write(titulo))
        self.play(FadeIn(bloque_pregunta))
        self.wait(1)
        self.play(Write(respuesta))
        self.play(Write(p1))
        self.play(Write(p2))
        self.wait(1)
        self.play(Create(box), Write(formula_final))
        self.wait(4)

class Creditos(Scene):
    def construct(self):
        titulo = Text("Referencias y Créditos", font_size=28, color=YELLOW).to_edge(UP)

        # Bloque de integrantes y roles
        t1 = Text("Integrantes (Grupo 11):", font_size=20, color=BLUE)
        integrantes = Text(
            "• Lucas: Explicación Matemática\n"
            "• Nicolás: Manim y Desarrollo de Código\n"
            "• Diego: README y Edición de Video",
            font_size=16, color=WHITE
        )

        # Bloque de fuentes bibliográficas
        t2 = Text("Bibliografía:", font_size=20, color=BLUE)
        biblio = Text(
            "• Stewart, J. (2012). Cálculo de una variable: Trascendentes tempranas.\n"
            "• Apuntes y material del curso MAT1134 - Cálculo Intermedio.",
            font_size=16, color=WHITE
        )

        # Bloque de software e Inteligencia Artificial
        t3 = Text("Herramientas y Declaración de IA:", font_size=20, color=BLUE)
        herramientas = Text(
            "• Animaciones generadas con Manim Community v0.18+ (Python).\n"
            "• Uso de IA Generativa para asistencia en sintaxis de Manim y guion.",
            font_size=16, color=WHITE
        )

        g1 = VGroup(t1, integrantes).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        g2 = VGroup(t2, biblio).arrange(DOWN, aligned_edge=LEFT, buff=0.1)
        g3 = VGroup(t3, herramientas).arrange(DOWN, aligned_edge=LEFT, buff=0.1)

        todo = VGroup(g1, g2, g3).arrange(DOWN, aligned_edge=LEFT, buff=0.3)
        todo.next_to(titulo, DOWN, buff=0.4)

        self.play(Write(titulo))
        self.play(FadeIn(g1))
        self.wait(1)
        self.play(FadeIn(g2))
        self.wait(1)
        self.play(FadeIn(g3))
        self.wait(4)