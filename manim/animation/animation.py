"""
Base class for all animations.
"""

from copy import deepcopy

import numpy as np

from ..mobject.mobject import Mobject
from ..utils.config_ops import digest_config
from ..utils.rate_functions import smooth

DEFAULT_ANIMATION_RUN_TIME = 1.0
DEFAULT_ANIMATION_LAG_RATIO = 0


class Animation:
    """Base class for animating Mobjects.

    Parameters
    ----------
    mobject : :class:`~.Mobject`
        The mobject to be animated.
    kwargs : :class:`dict`
        Arguments to be consumed by :func:`~digest_config`.

    """

    CONFIG = {
        "run_time": DEFAULT_ANIMATION_RUN_TIME,
        "rate_func": smooth,
        "name": None,
        # Does this animation add or remove a mobject form the screen
        "remover": False,
        # If 0, the animation is applied to all submobjects
        # at the same time
        # If 1, it is applied to each successively.
        # If 0 < lag_ratio < 1, its applied to each
        # with lagged start times
        "lag_ratio": DEFAULT_ANIMATION_LAG_RATIO,
        "suspend_mobject_updating": True,
    }

    def __init__(self, mobject, **kwargs):
        assert isinstance(mobject, Mobject)
        digest_config(self, kwargs)
        self.mobject = mobject

    def __str__(self):
        if self.name:
            return self.name
        return self.__class__.__name__ + str(self.mobject)

    def begin(self):
        """Start the animation.

        Notes
        -----
        This is called internally by manim when rendering a Scene.

        See Also
        --------
        :func:`~finish`
        """
        # Perform here as much initialization as possible, especially any
        # mobject copying.
        self.starting_mobject = self.create_starting_mobject()
        if self.suspend_mobject_updating:
            # All calls to self.mobject's internal updaters
            # during the animation, either from this Animation
            # or from the surrounding scene, should do nothing.
            # It is, however, okay and desirable to call
            # the internal updaters of self.starting_mobject,
            # or any others among self.get_all_mobjects()
            self.mobject.suspend_updating()
        self.interpolate(0)

    def finish(self):
        """End the animation.

        Notes
        -----
        This is called internally by manim when rendering a Scene.

        See Also
        --------
        :func:`~begin`
        """
        self.interpolate(1)
        if self.suspend_mobject_updating:
            self.mobject.resume_updating()

    def clean_up_from_scene(self, scene):
        """Perform clean up, usually after the animation has finished.

        Notes
        -----
        This is called internally by manim when rendering a Scene.

        Parameters
        ----------
        scene : :class:`~.Scene`
            The scene that is rendering this animation.

        """
        if self.remover:
            scene.remove(self.mobject)

    def create_starting_mobject(self):
        """Create a Mobject that represents the initial state of the animation.

        Returns
        -------
        :class:`tuple`
            The mobjects.
        """
        return self.mobject.copy()

    def get_all_mobjects(self):
        """Return all mobjects handled by this animation.

        Returns
        -------
        :class:`tuple`
            The mobjects.

        Notes
        -----
        Ordering of the returned tuple must match the ordering of arguments to
        :func:`~interpolate_submobject`.

        See Also
        --------
        :func:`~interpolate_submobject`
        """
        return self.mobject, self.starting_mobject

    def get_all_families_zipped(self):
        """Zip all of the mobjects' families.

        Returns
        -------
        :class:`zip`
            All of the mobjects handled by this animation, zipped.

        """
        return zip(
            *[mob.family_members_with_points() for mob in self.get_all_mobjects()]
        )

    def update_mobjects(self, dt):
        """Update each mobject in self.get_all_mobjects().

        Parameters
        ----------
        dt : `float`
            The fraction of the animation that has transpired, to be passed on
            to each Mobject's update function.

        Notes
        -----
        Typically, self.mobject will have its updating suspended during the
        animation, so this function does not update it.

        See Also
        --------
        :func:`~get_all_mobjects`, :func:`~Mobject.update`

        """
        # The surrounding scene typically handles updating of self.mobject
        for mob in self.get_all_mobjects():
            if mob is not self.mobject:
                mob.update(dt)

    def copy(self):
        """Return a deepcopy of the animation.

        Returns
        -------
        :class:`~Animation`
            A copy of this animation.

        """
        return deepcopy(self)

    def update_config(self, **kwargs):
        digest_config(self, kwargs)
        return self

    def interpolate(self, alpha):
        """Interpolate mobjects by evaluating the rate function at alpha.

        Parameters
        ----------
        alpha : :float:
            The time at which the rate function will be evaluated.

        See Also
        --------
        :func:`~interpolate_mobject`

        """
        self.interpolate_mobject(self.rate_func(np.clip(alpha, 0, 1)))

    def update(self, alpha):
        """Kept for backwards compatibility.

        .. deprecated:: 0.0.1
          `update` will be removed in manim-ce 1.0.0, it is replaced by
          :func:`~interpolate`.

        """
        self.interpolate(alpha)

    def interpolate_mobject(self, alpha):
        families = list(self.get_all_families_zipped())
        for i, mobs in enumerate(families):
            sub_alpha = self.get_sub_alpha(alpha, i, len(families))
            self.interpolate_submobject(*mobs, sub_alpha)

    def interpolate_submobject(self, submobject, starting_sumobject, alpha):
        # Typically ipmlemented by subclass
        pass

    def get_sub_alpha(self, alpha, index, num_submobjects):
        # TODO, make this more understanable, and/or combine
        # its functionality with AnimationGroup's method
        # build_animations_with_timings
        lag_ratio = self.lag_ratio
        full_length = (num_submobjects - 1) * lag_ratio + 1
        value = alpha * full_length
        lower = index * lag_ratio
        return np.clip((value - lower), 0, 1)
