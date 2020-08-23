HelloExample
============

ImageExampleGit
***********************

.. code-block:: python

    class TestExample(Scene):
        def construct(self):
            dot = Dot()
            self.add(dot)

.. raw:: html

    <img src="https://raw.githubusercontent.com/kolibril13/manim-snippets/master/Shapes-Geometrie/ShapeExample1.png" style="width:560px;height:315px;">



VideoExampleGit
***********************

.. code-block:: python

    class TestExample2(Scene):
        def construct(self):
            sq = Square()
            self.add(sq)
            self.play(Transform(sq,Circle()))

.. raw:: html

    <video width="560" height="315" controls>
        <source src="https://github.com/Elteoremadebeethoven/manim_3feb_docs.github.io/blob/master/source/videos/ApplyMethodExample.mp4?raw=true" type="video/mp4">
    </video>

