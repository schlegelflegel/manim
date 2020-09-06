from manim.scene.scene import Scene
from manim.mobject.svg.text_mobject import TextMobject

class SectionOne(Scene):
    def construct(self):
        self.add(TextMobject("Section 1: Seeing with your ears"))
        self.wait()
