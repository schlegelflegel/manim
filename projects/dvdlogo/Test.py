import os
import sys
PROJECT_DIR = os.path.dirname(__file__)
sys.path.append(PROJECT_DIR)

from manim import *
import theme

class DVDLogo(Rectangle):
    CONFIG = {
        "width": 2,
        "height": 2,
        "color": theme.ORANGE_DARK,
        "fill_opacity": 0.3,
        "svg_config": {
            "fill_color": theme.ORANGE,
            "stroke_width": 0,
            "file_name": os.path.join(PROJECT_DIR, "assets/DVD_Video_Logo.svg")
        },
        "offset": 0
    }

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.svg = SVGMobject(**self.svg_config)
        self.svg.set_width(self.get_width() * 0.9)

        self.add(self.svg)

class Test(Scene):
    def construct(self):
        self.logo = DVDLogo()

        self.add(self.logo)
        self.wait()
