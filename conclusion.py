from manim import *
import numpy as np
import random

class concl(Scene):
    def construct(self):
        myTemplate = TexTemplate()
        myTemplate.add_to_preamble(r"\usepackage{mathdots}")
        myTemplate.add_to_preamble(r"\usepackage[lite]{mtpro2}")

        random.seed(1)

        text1 = MarkupText("Recap on buffer solutions:", font="Arno Pro", font_size=36).to_edge(UL)

        text2 = MarkupText("· Buffers are weak acid/base + conjugate base/acid.", font="Arno Pro", font_size=36).to_edge(UL).shift(1 * DOWN)

        text3 = MarkupText("· They resist pH change by neutralizing added acids or bases.", font="Arno Pro", font_size=36).to_edge(UL).shift(1.8 * DOWN)

        text4 = MarkupText("· The log of the concentrations are their escaping tendencies.", font="Arno Pro", font_size=36).to_edge(UL).shift(2.6 * DOWN)

        text5 = MarkupText("· Escaping tendencies of each species are related through the \n  Henderson-Hasselbalch equation.", font="Arno Pro", font_size=36).to_edge(UL).shift(3.4 * DOWN)

        text6 = MarkupText("· Diluting buffers do not change its pH.", font="Arno Pro", font_size=36).to_edge(UL).shift(4.7 * DOWN)

        text7 = MarkupText("· Strongest buffer occurs when [HA] ≈ [A<sup>-</sup>].", font="Arno Pro", font_size=36).to_edge(UL).shift(5.5 * DOWN)

        self.play(Write(text1))
        self.wait(2)
        self.play(Write(text2))
        self.wait(5)
        self.play(Write(text3))
        self.wait(4)
        self.play(Write(text4))
        self.wait(5)
        self.play(Write(text5))
        self.wait(4)
        self.play(Write(text6))
        self.wait(4)
        self.play(Write(text7))
        self.wait(2)


        self.wait()
        self.wait()


%manim -qh -v WARNING concl