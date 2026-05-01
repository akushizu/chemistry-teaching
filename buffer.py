from manim import *
import numpy as np
import random

class buff(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathdots}")
        myTemplate.add_to_preamble(r"\usepackage[lite]{mtpro2}")

        random.seed(1)

        text1 = MarkupText("Let's apply these to a buffer solution of HA and A<sup>-</sup>", font="Arno Pro", font_size=36).to_edge(UL)

        eq1 = MathTex(r"\text{HA}", r"\rightleftharpoons", r"\text{H}^+", "+", r"\text{A}^-", tex_template=myTemplate)

        eq2 =  MathTex(r"\log [\text{H}^+]", "=", r"\log K_a", "-", r"\log [\text{A}^-]", "+", r"\log [\text{HA}]", tex_template=myTemplate)

        eq3 =  MathTex(r"-\log [\text{H}^+]", "=", r"-\log K_a", "+", r"\log \frac{[\text{A}^-]}{[\text{HA}]}", tex_template=myTemplate)

        text2 = Text("The equation of log K for the buffer is:", font="Arno Pro", font_size=36).to_edge(UL)

        text3 = Text("The equation of log K can be written in a more common form:", font="Arno Pro", font_size=36).to_edge(UL)

        text4 = Text("The Henderson-Hasselbalch equation.", font="Arno Pro", font_size=36).to_edge(UL)

        text5 = Text("Let's revert to the previous form for our purposes.", font="Arno Pro", font_size=36).to_edge(UL)

        self.play(Write(text1))
        self.wait()
        self.play(FadeIn(eq1))
        self.play(eq1.animate.move_to(2.5 * UP))
        self.wait(2)
        self.remove(text1)
        self.play(Write(text2))
        self.wait()
        self.play(FadeIn(eq2))
        self.wait()
        self.remove(text2)
        self.play(Write(text3))
        self.wait()
        self.play(TransformMatchingShapes(eq2, eq3))
        self.wait()
        self.remove(text3)
        self.play(Write(text4))
        self.wait(3)
        self.remove(text4)
        self.play(Write(text5))
        self.wait()
        self.play(TransformMatchingShapes(eq3, eq2))
        self.play(eq2.animate.move_to(1.5 * UP))
        self.wait(2)

        text6 = Text("Let's plot the escaping tendencies of each species.", font="Arno Pro", font_size=36).to_edge(UL)

        chart1 = BarChart(
            values=[2, 2, 7, 7],
            bar_names=["logK", "log[H+]", "log[HA]", "log[A-]"],
            y_range=[0, 10, 4],
            y_length=2,
            x_length=4,
            bar_colors=['#003f5c', '#58508d', '#bc5090', '#ff6361'],
            x_axis_config={"font_size": 24}
        ).shift(DOWN)

        text7 = MarkupText("Notice the big gap between H<sup>+</sup> and others.", font="Arno Pro", font_size=36).to_edge(UL)

        arrow1 = Arrow(np.array([-0.5, -0.3, 0]), np.array([-0.5, -1.8, 0]), stroke_width=9)

        text8 = Text("This is common for most weak acids, and is beneficial in calculations.", font="Arno Pro", font_size=36).to_edge(UL)

        self.remove(text5)
        self.play(Write(text6))
        self.wait(2)
        self.play(Write(chart1))
        self.wait(2)
        self.remove(text6)
        self.play(Write(text7))
        self.wait()
        self.play(GrowArrow(arrow1))
        self.wait(2)
        self.remove(text7)
        self.play(Write(text8))
        self.wait(4)

        text9 = Text("What happends if we add some acid?", font="Arno Pro", font_size=36).to_edge(UL)

        mv1 = chart1.animate.change_bar_values([2, 4, 7, 7], update_colors=True)

        arrow2 = Arrow(np.array([-0.5, -1.4, 0]), np.array([-0.5, -0.2, 0]), stroke_width=9)

        self.remove(text8, arrow1)
        self.play(Write(text9))
        self.wait()
        self.play(mv1, GrowArrow(arrow2))
        self.play(Flash(chart1[0][1].get_center() + np.array([0, 0.4, 0.])), Flash(eq1.get_center()), run_time=0.5)
        self.play(Flash(chart1[0][1].get_center() + np.array([0, 0.4, 0.])), Flash(eq1.get_center()), run_time=0.5)
        self.wait()

        text10 = Text("The Le Chatelier's principle will push it back.", font="Arno Pro", font_size=36).to_edge(UL)

        mv2 = chart1.animate.change_bar_values([2, 2, 7, 7], update_colors=True)

        arrow3 = Arrow(np.array([-0.5, -0.4, 0]), np.array([-0.5, -1.6, 0]), stroke_width=9)

        text11 = Text("Notice these escaping tendencies/concentration barely change?", font="Arno Pro", font_size=36).to_edge(UL)

        arrow4 = Arrow(np.array([3.2, -0.6, 0]), np.array([1.7, -0.6, 0]), stroke_width=9)

        text12 = Text("Remember this is log scale of concentrations.", font="Arno Pro", font_size=36).to_edge(UL)

        text13 = Text("The difference is in several orders of magnitudes!", font="Arno Pro", font_size=36).to_edge(UL)

        text14 = Text("Lesson: buffers can resist pH change.", font="Arno Pro", font_size=36).to_edge(UL)

        self.remove(text9, arrow2)
        self.play(Write(text10))
        self.wait()
        self.play(mv2, GrowArrow(arrow3))
        self.wait()
        self.remove(text10, arrow3)
        self.play(Write(text11))
        self.wait()
        self.play(GrowArrow(arrow4))
        self.wait()
        self.remove(text11)
        self.play(Write(text12))
        self.wait(3)
        self.remove(text12)
        self.play(Write(text13))
        self.wait(3)
        self.remove(text13)
        self.play(Write(text14))
        self.wait(3)

        text15 = Text("What happens if we dilute the buffer by half?", font="Arno Pro", font_size=36).to_edge(UL)

        mv3 = chart1.animate.change_bar_values([2, 2, 6.6, 6.6], update_colors=True)

        arrow5 = Arrow(np.array([1.0, 0.7, 0]), np.array([1.0, -0.8, 0]), stroke_width=9)

        eq4 =  MathTex(r"\log [\text{H}^+]", "=", r"\log K_a", "-", r"\log \frac{[\text{A}^-]}{2}", "+", r"\log \frac{[\text{HA}]}{2}", tex_template=myTemplate).shift(eq2.get_center())

        eq5 =  MathTex(r"\log [\text{H}^+]", "=", r"\log K_a", "-", r"\log [\text{A}^-]", "+", r"\log 2", "+", r"\log [\text{HA}]", "-", r"\log 2", tex_template=myTemplate).shift(eq2.get_center())

        text16 = Text("Lesson: diluting a buffer does not change its pH.", font="Arno Pro", font_size=36).to_edge(UL)

        self.remove(text14, arrow4)
        self.play(Write(text15))
        self.wait()
        self.play(mv3, GrowArrow(arrow5))
        self.wait()
        self.play(TransformMatchingShapes(eq2, eq4))
        self.wait(2)
        self.play(TransformMatchingShapes(eq4, eq5))
        self.wait(2)
        self.play(TransformMatchingShapes(eq5, eq2))
        self.wait(2)
        self.remove(text15)
        self.play(Write(text16))
        self.wait(3)

        text17 = Text("How much amount of acid can a buffer take while resisting pH change?", font="Arno Pro", font_size=36).to_edge(UL)

        text18 = Text("In order for pH to change by 1,...", font="Arno Pro", font_size=36).to_edge(UL)

        text19 = MarkupText("... we need to increase the diffenence of the escaping tendencies of \nHA and A<sup>-</sup> by 1.", font="Arno Pro", font_size=36).to_edge(UL)

        mv4 = chart1.animate.change_bar_values([2, 3, 6.8, 5.8], update_colors=True)

        arrow6 = Arrow(np.array([-0.5, -1.5, 0]), np.array([-0.5, 0.3, 0]), stroke_width=9)
        arrow7 = Arrow(np.array([0.5, -0.8, 0]), np.array([0.5, 0.6, 0]), stroke_width=9)
        arrow8 = Arrow(np.array([1.5, 0.5, 0]), np.array([1.5, -1.0, 0]), stroke_width=9)

        text20 = MarkupText("In terms of concentrations, the difference of [HA] and [A<sup>-</sup>] \nare made 10 times.", font="Arno Pro", font_size=36).to_edge(UL)

        text21 = MarkupText("The mole change of them is about the same as their \ninitial amount of moles.", font="Arno Pro", font_size=36).to_edge(UL)

        text22 = Text("This is the idea of buffer capacity.", font="Arno Pro", font_size=36).to_edge(UL)

        text23 = MarkupText("Rule of thumb: We need roughly the same amount of H<sup>+</sup> as HA \nto change the pH by 1.", font="Arno Pro", font_size=36).to_edge(UL)

        self.remove(text16, arrow5)
        self.play(Write(text17))
        self.wait(5)
        self.remove(text17)
        self.play(Write(text18))
        self.wait(3)
        self.remove(text18)
        self.play(Write(text19))
        self.wait(5)
        self.play(mv4, GrowArrow(arrow6), GrowArrow(arrow7), GrowArrow(arrow8))
        self.wait()
        self.remove(text19)
        self.play(Write(text20))
        self.wait(6)
        self.remove(text20)
        self.play(Write(text21))
        self.wait(5)
        self.remove(text21)
        self.play(Write(text22))
        self.wait(4)
        self.remove(text22)
        self.play(Write(text23))
        self.wait(8)

        text24 = Text("When will the buffer capacity become the greatest?", font="Arno Pro", font_size=36).to_edge(UL)

        text25 = MarkupText("When both log[HA] and log[A<sup>-</sup>] is furthest away from log[H<sup>+</sup>].", font="Arno Pro", font_size=36).to_edge(UL)

        mv5 = chart1.animate.change_bar_values([2, 2, 7, 7], update_colors=True)

        arrow9 = Arrow(np.array([1.0, -0.8, 0]), np.array([1.0, 0.7, 0]), stroke_width=9)

        text26 = MarkupText("Lesson: buffer capacity maximizes when [HA] = [A<sup>-</sup>].", font="Arno Pro", font_size=36).to_edge(UL)

        text27 = Text("These are the basics of a buffer solution.", font="Arno Pro", font_size=36).to_edge(UL)

        self.remove(text23, arrow6, arrow7, arrow8)
        self.play(Write(text24))
        self.wait(3)
        self.remove(text24)
        self.play(Write(text25))
        self.wait(6)
        self.play(mv5, GrowArrow(arrow9))
        self.wait(3)
        self.remove(text25, arrow9)
        self.play(Write(text26))
        self.wait(6)
        self.remove(text26, arrow9)
        self.play(Write(text27))
        self.wait(2)

       
        self.wait()
        self.wait()


%manim -qh -v WARNING buff