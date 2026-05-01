from manim import *
import numpy as np
import random

class theo(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathdots}")
        myTemplate.add_to_preamble(r"\usepackage[lite]{mtpro2}")

        random.seed(1)

        text1 = Text("Let's go into the theory.", font="Arno Pro", font_size=36).to_edge(UL)
        text2 = Text("First things first.", font="Arno Pro", font_size=36).to_edge(UL)
        text3 = Text("Quick words on equilibrium.", font="Arno Pro", font_size=36).next_to(text2, RIGHT)

        self.play(Write(text1))
        self.wait(2)
        self.remove(text1)
        self.play(Write(text2))
        self.wait(2)
        self.play(Write(text3))
        self.wait(2)

        eq1 = MathTex(
            r"""\alpha A + \beta B \rightleftharpoons \gamma C + \delta D""",
            tex_template=myTemplate
        )

        eq2 = MathTex(
            r"""\alpha A + \beta B \rightleftharpoons \gamma C + \delta D""",
            r"""\qquad K = \frac{[C]^\gamma [D]^\delta}{[A]^\alpha [B]^\beta}""",
            tex_template=myTemplate
        )

        self.play(Write(eq1))
        self.play(TransformMatchingTex(eq1, eq2))
        self.wait(2)

        text4 = Text("Isn't the expression of  K  looks inelegant?", font="Arno Pro", font_size=36).to_edge(UL)

        eq3 =  MathTex(
            "K = ",
            r"""\frac{[C]^\gamma [D]^\delta}{[A]^\alpha [B]^\beta}""",
            tex_template=myTemplate
        )

        eq1 = eq1.to_edge(UP).shift(DOWN)

        self.remove(text2, text3)
        self.play(Write(text4))
        self.wait(2)
        self.play(TransformMatchingTex(eq2, Group(eq1, eq3)))
        self.wait()

        text5 = Text("After taking the logarithm, ...", font="Arno Pro", font_size=36).to_edge(UL)
        text6 = Text("Nice!", font="Arno Pro", font_size=36).next_to(text5, RIGHT)

        eq4 =  MathTex(r"\log ", "K = ", r"- \alpha\log [A] - \beta\log [B] + \gamma\log [C] + \delta\log [D]", tex_template=myTemplate)

        self.remove(text4)
        self.play(Write(text5))
        self.wait()

        self.play(TransformMatchingTex(eq3, eq4))
        self.wait()
        self.play(Write(text6))
        self.wait(2)

        text7 = Text("These 'log[X]'s appear like temperature.", font="Arno Pro", font_size=36).to_edge(UL)
        text8 = Text("Why?", font="Arno Pro", font_size=36).to_edge(UL)
        text9 = Text("Let's plot these 'temperatures'.", font="Arno Pro", font_size=36).next_to(text8)
        
        self.remove(text5, text6)
        self.play(Write(text7))
        self.wait(2)
        self.remove(text7)
        self.play(Write(text8))
        self.wait()
        self.play(Write(text9))
        self.wait()

        chart1 = BarChart(
            values=[0, 5, 4.8, 1.2, 1.5],
            bar_names=["logK", "log[A]", "log[B]", "log[C]", "log[D]"],
            y_range=[0, 6, 3],
            y_length=2,
            x_length=4,
            bar_colors=['#003f5c', '#58508d', '#bc5090', '#ff6361', '#ffa600'],
            x_axis_config={"font_size": 24}
        ).shift(DOWN)

        rect = Rectangle(width=0.6, height=0.3, color=BLACK, fill_opacity=1).shift(np.array([-1.6 ,-2.35 ,0 ]))

        d1 = Dot(point=np.array([-1.9, 0.8, 0.]), radius=0.1, color='#58508d')
        d2 = Dot(point=np.array([-0.6, 0.8, 0.]), radius=0.1, color='#bc5090')

        d3 = Dot(point=np.array([0.9, 0.8, 0.]), radius=0.1, color='#ff6361')
        d4 = Dot(point=np.array([2.1, 0.8, 0.]), radius=0.1, color='#ffa600')

        mv1 = chart1.animate.change_bar_values([0, 4.6, 4.5, 1.5, 2.0], update_colors=True)

        self.play(eq4.animate.shift(UP), Write(chart1))
        self.add(rect)
        self.play(eq1.animate.shift(DOWN), FadeOut(eq4))
        self.play(FadeIn(d1, d2))
        self.wait()

        text10 = Text("When reaction occurs, the 'temperature' of the reactants drop,", font="Arno Pro", font_size=36).to_edge(UL)

        arrow1 = Arrow(np.array([-0.4, 0.7, 0]), np.array([-0.4, -0.7, 0]), stroke_width=9)
        arrow2 = Arrow(np.array([1.2, -1.5, 0]), np.array([1.2, -0.2, 0]), stroke_width=9)

        text11 = Text("and the 'temperature' of the products rise.", font="Arno Pro", font_size=36).to_edge(UL).shift(DOWN)

        self.remove(text8, text9)
        self.play(Write(text10))
        self.wait(2)
        self.play(Write(text11))
        self.wait()
        self.play(TransformMatchingShapes(Group(d1, d2), Group(d3, d4)), mv1, GrowArrow(arrow1), GrowArrow(arrow2))
        self.wait(2)

        text12 = Text("These 'temperatures' are actually each species' ", font="Arno Pro", font_size=36).to_edge(UL)

        text13 = Text(" escaping tendency.", color=BLUE, font="Arno Pro", font_size=36).next_to(text12)
        
        label1 = chart1.get_y_axis_label(Text("escaping tendency", font="Arno Pro", font_size=24).rotate(90 * DEGREES), edge=LEFT, direction=LEFT)

        self.remove(text10, text11, arrow1, arrow2)
        self.play(Write(text12))
        self.play(Write(text13))
        self.wait(2)
        self.add(chart1, label1)
        self.remove(rect)
        self.add(rect)
        self.wait()

        text14 = Text("The higher the escaping tendency, the more likely to react, or ", font="Arno Pro", font_size=36).to_edge(UL)

        text15 = Text("'escape'.", color=BLUE, font="Arno Pro", font_size=36).next_to(text14)

        eq5 = MathTex(
            r"""\alpha A + \beta B \rightarrow \gamma C + \delta D""",
            tex_template=myTemplate
        ).shift(eq1.get_center())

        arrow3 = Arrow(np.array([-1.2, 0.8, 0]), np.array([0.5, 0.8, 0]), stroke_width=9)

        self.remove(text12, text13)
        self.play(Write(text14))
        self.play(Write(text15))
        self.wait(3)

        self.remove(eq1)
        self.add(eq5)

        self.play(Flash(chart1[0][1].get_center() + np.array([0, 0.8, 0.])), Flash(chart1[0][2].get_center() + np.array([0, 0.8, 0.])), GrowArrow(arrow3), run_time=0.5)
        self.play(Flash(chart1[0][1].get_center() + np.array([0, 0.8, 0.])), Flash(chart1[0][2].get_center() + np.array([0, 0.8, 0.])), run_time=0.5)

        self.wait(2)

        text16 = Text("At equilibrium, the weighted sum of the escaping tendency is the smallest.", font="Arno Pro", font_size=36).to_edge(UL)

        text17 = Text("This minimum is the logarithm of the equilibrium constant K.", font="Arno Pro", font_size=36).to_edge(UL)

        mv2 = chart1.animate.change_bar_values([3, 4.6, 4.5, 1.5, 2.0], update_colors=True)

        self.remove(text14, text15)
        self.play(Write(text16))
        self.wait(4)
        self.remove(text16)
        self.play(Write(text17))
        self.wait(4)
        self.remove(rect)
        self.play(mv2)
        self.remove(eq5)
        self.add(eq1)
        self.play(FadeOut(d3), FadeOut(d4), FadeOut(arrow3), FadeIn(eq4), eq1.animate.shift(UP))
        self.wait(2)

        text18 = Text("Next, let's talk about the Le Chatelier's principle.", font="Arno Pro", font_size=36).to_edge(UL)

        text19 = Text("When we add A into the solution, the escaping tendency rises.", font="Arno Pro", font_size=36).to_edge(UL)

        eq6 = MathTex(r"\alpha", "A", r"+ \beta", "B", r"\rightleftharpoons", r"\gamma", "C", r"+ \delta", "D", tex_template=myTemplate)

        eq7 = MathTex(r"\alpha", r"\textsl{\Large A}", r"+ \beta", "B", r"\rightleftharpoons", r"\gamma", "C", r"+ \delta", "D", tex_template=myTemplate)

        mv3 = chart1.animate.change_bar_values([3, 5, 4.5, 1.5, 2.0], update_colors=True)

        arrow4 = Arrow(np.array([-0.8, -0.5, 0]), np.array([-0.8, 0.7, 0]), stroke_width=9)

        self.remove(text17)
        self.play(Write(text18), FadeOut(eq4), eq1.animate.shift(DOWN))
        self.remove(eq1)
        self.add(eq6.shift(eq1.get_center()))
        self.wait(3)
        self.remove(text18)
        self.play(Write(text19))
        self.wait()
        self.play(TransformMatchingTex(eq6, eq7.shift(eq6.get_center())), GrowArrow(arrow4), mv3)
        self.wait(4)
        
        text20 = Text("The rise in tendency forces the reaction to move forward.", font="Arno Pro", font_size=36).to_edge(UL)

        mv4 = chart1.animate.change_bar_values([3, 4.8, 4.3, 1.8, 2.3], update_colors=True)

        text21 = Text("It pushes the reaction towards equilibrium again.", font="Arno Pro", font_size=36).to_edge(UL)

        text22 = Text("Note that K is constant.", font="Arno Pro", font_size=36).to_edge(UL).shift(0.8 * DOWN)

        text23 = Text("This is the Le Chatelier's principle.", font="Arno Pro", font_size=36).to_edge(UL)

        self.remove(text19, arrow4)
        self.play(Write(text20))
        self.wait()
        self.play(TransformMatchingTex(eq7, eq6), GrowArrow(arrow1), GrowArrow(arrow2), GrowArrow(arrow3), mv4)
        self.wait(2)
        self.remove(text20)
        self.play(Write(text21))
        self.wait()
        self.play(Write(text22))
        self.wait(3)
        self.remove(text21, text22, arrow1, arrow2, arrow3)
        self.play(Write(text23))
        self.wait(2)



        self.wait()
        self.wait()


%manim -qh -v WARNING theo