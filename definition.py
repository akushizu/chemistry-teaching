from manim import *
import numpy as np
import random

class defi(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage[lite]{mtpro2}")

        random.seed(1)

        text1 = Text("A buffer solution is a solution composed of", font="Arno Pro", font_size=36).to_edge(UL)
        text2 = Text("· weak acid/base", font="Arno Pro", font_size=36).to_edge(UL).shift(0.8 * DOWN)
        text3 = Text("· its conjugate base/acid", font="Arno Pro", font_size=36).to_edge(UL).shift(1.4 * DOWN)

        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait()
        self.play(Write(text3))
        self.wait(3)

        leg1 = Dot(point=np.array([-5.5, 0, 0.]), radius=0.08, color=WHITE)
        leg2 = Dot(point=np.array([-5.5, -0.5, 0.]), radius=0.2, color=BLUE)
        leg3a = Dot(point=np.array([-5.45, -1, 0.]), radius=0.2, color=BLUE)
        leg3b = Dot(point=np.array([-5.65, -1, 0.]), radius=0.08, color=WHITE)
        lega = MarkupText("H<sup>+</sup>", font="Arno Pro", font_size=36).next_to(leg1).shift(0.2 * RIGHT)
        legb = MarkupText("A<sup>-</sup>", font="Arno Pro", font_size=36).next_to(leg2).shift(0.1 * RIGHT)
        legc = MarkupText("HA", font="Arno Pro", font_size=36).next_to(leg3a).shift(0.05 * RIGHT)

        amcoor = [np.array([(random.random() - 0.5) * 7 + 2.5, (random.random() - 0.5) * 4 - 1, 0.]) for _ in range(10)]
        hacoor = [np.array([(random.random() - 0.5) * 7 + 2.5, (random.random() - 0.5) * 4 - 1, 0.]) for _ in range(10)]
        hpcoor = hacoor + [np.array([(random.random() - 0.5) * 7 + 2.5, (random.random() - 0.5) * 4 - 1, 0.]) for _ in range(2)]

        am = [Dot(point=i, radius=0.2, color=BLUE) for i in amcoor]
        ha = [Dot(point=i, radius=0.2, color=BLUE) for i in hacoor]
        hp = [Dot(point=i, radius=0.08, color=WHITE).shift(0.2 * LEFT) for i in hpcoor]

        self.play(FadeIn(leg1), FadeIn(lega))
        self.play(FadeIn(leg2), FadeIn(legb))
        self.play(FadeIn(leg3a), FadeIn(leg3b), FadeIn(legc))

        self.play(FadeIn(*am), FadeIn(*ha), FadeIn(*hp))
        self.wait()

        text4 = Text("A buffer can resists pH change when acid or base is added.", font="Arno Pro", font_size=36).to_edge(UL)

        self.remove(text1, text2, text3)
        self.play(Write(text4))
        self.wait(5)

        text5 = MarkupText("When acid is added, A<sup>-</sup> will neutralize the incomming H<sup>+</sup>", font="Arno Pro", font_size=36).to_edge(UL)

        ahpcoor = [np.array([2.5+0.2*i, 1.5, 0.]) for i in np.arange(5)]
        ahp = [Dot(point=i, radius=0.08, color=WHITE) for i in ahpcoor]

        text5 = MarkupText("When acid is added, A<sup>-</sup> will neutralize the incomming H<sup>+</sup>", font="Arno Pro", font_size=36).to_edge(UL)

        self.remove(text4)
        self.play(Write(text5))
        self.wait(4)

        self.play(FadeIn(*ahp))
        neu1 = [ahp[i].animate.move_to(amcoor[i] - np.array([0.2, 0., 0.])) for i in range(len(ahp))]
        self.play(*neu1)
        self.wait()
        
        text6 = MarkupText("Remember that HA is a weak acid, so it can take up H<sup>+</sup> \nwithout dissociating.", font="Arno Pro", font_size=36).to_edge(UL)

        circ1 = Circle(radius=0.7).shift(amcoor[3])

        self.remove(text5)
        self.play(Write(text6))
        self.wait()
        self.play(FadeIn(circ1))
        self.wait(5)

        text7 = MarkupText("On the other hand, when base is added,\nHA will neutralize the incomming OH<sup>-</sup>", font="Arno Pro", font_size=36).to_edge(UL)

        leg4 = Dot(point=np.array([-5.5, -1.5, 0.]), radius=0.2, color=RED)
        legd = MarkupText("OH<sup>-</sup>", font="Arno Pro", font_size=36).next_to(leg4).shift(0.1 * RIGHT)

        aohcoor = [np.array([2.5+0.4*i, 1.5, 0.]) for i in np.arange(5)]
        aoh = [Dot(point=i, radius=0.2, color=RED) for i in aohcoor]

        text8 = MarkupText("OH<sup>-</sup> took the H<sup>+</sup> from HA.", font="Arno Pro", font_size=36).to_edge(UL)

        text9 = MarkupText("Again, HA is a weak acid, and A<sup>-</sup> is also a weak base.", font="Arno Pro", font_size=36).to_edge(UL)

        circ2 = Circle(radius=0.7).shift(amcoor[3] + np.array([0, 0.25, 0.]))

        leg5a = Dot(point=np.array([-5.45, -2, 0.]), radius=0.2, color=RED)
        leg5b = Dot(point=np.array([-5.65, -2, 0.]), radius=0.08, color=WHITE)
        lege = MarkupText("H<sub>2</sub>O", font="Arno Pro", font_size=36).next_to(leg5a).shift(0.05 * RIGHT)

        water = [Dot(point=(amcoor[3] + np.array([0.05, 0.5, 0.])), radius=0.2, color=RED), Dot(point=(amcoor[3] + np.array([-0.15, 0.5, 0.])), radius=0.08, color=WHITE)]

        text10 = MarkupText("A<sup>-</sup> cannot easily take H<sup>+</sup> from water.", font="Arno Pro", font_size=36).to_edge(UL)

        self.remove(text6, circ1)
        self.play(Write(text7))
        self.wait(3)
        self.play(FadeIn(leg4), FadeIn(legd))
        self.play(FadeIn(*aoh))
        self.wait()

        neu2 = [aoh[i].animate.move_to(amcoor[i] - np.array([0.2, 0., 0.])) for i in range(len(aoh))]
        self.play(*neu2)

        self.remove(text7)
        self.play(Write(text8))
        self.wait(2)

        self.play(FadeOut(*ahp), FadeOut(*aoh))
        self.wait()
        
        self.remove(text8)
        self.play(Write(text9))
        self.wait(4)

        self.play(FadeIn(*water), FadeIn(leg5a), FadeIn(leg5b), FadeIn(lege))
        self.wait()

        self.remove(text9)
        self.play(Write(text10))
        self.play(FadeIn(circ2))
        self.wait(3)

        text11 = Text("Therefore, the pH of a buffer will not easily change.", font="Arno Pro", font_size=36).to_edge(UL)

        text12 = Text("Now you have learned the basics of a buffer solution.", font="Arno Pro", font_size=36).to_edge(UL)

        self.remove(text10, circ2, *water)
        self.play(Write(text11))
        self.wait(5)
        self.remove(text11)
        self.play(Write(text12))
        self.wait(2)

        

        self.wait()
        self.wait()


%manim -qh -v WARNING defi