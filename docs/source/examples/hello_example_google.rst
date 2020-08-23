HelloExample
============

ImageExampleGOOGLE
***********************

.. code-block:: python

    class TestExample(Scene):
        def construct(self):
            dot = Dot()
            self.add(dot)

.. raw:: html

    <img src="https://drive.google.com/u/0/uc?id=1MB_VIhCX5IRDLXNimyPZ0uqPRF68VZ21&export=download" style="width:560px;height:315px;">



VideoExampleGOOLGE
***********************

.. code-block:: python

    class TestExample2(Scene):
        def construct(self):
            sq = Square()
            self.add(sq)
            self.play(Transform(sq,Circle()))

.. raw:: html

    <video width="560" height="315" controls>
        <source src="https://drive.google.com/u/0/uc?id=1yCp-xKnjN1z_giJqw7oEmDXQN4b0EBcp&export=download" type="video/mp4">
    </video>

