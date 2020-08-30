"""
Constant definitions.
"""

import numpy as np


# Messages
NOT_SETTING_FONT_MSG = """
You haven't set font.
If you are not using English, this may cause text rendering problem.
You set font like:
text = Text('your text', font='your font')
or:
class MyText(Text):
    CONFIG = {
        'font': 'My Font'
    }
"""
SCENE_NOT_FOUND_MESSAGE = """
   {} is not in the script
"""
CHOOSE_NUMBER_MESSAGE = """
Choose number corresponding to desired scene/arguments.
(Use comma separated list for multiple entries)
Choice(s): """
INVALID_NUMBER_MESSAGE = "Invalid scene numbers have been specified. Aborting."
NO_SCENE_MESSAGE = """
   There are no scenes inside that module
"""

# Cairo stuff
NORMAL = "NORMAL"
ITALIC = "ITALIC"
OBLIQUE = "OBLIQUE"
BOLD = "BOLD"

# Geometry: directions
ORIGIN = np.array((0.0, 0.0, 0.0))
"""The center of the coordinate system."""

UP = np.array((0.0, 1.0, 0.0))
"""One unit step in the positive Y direction."""

DOWN = np.array((0.0, -1.0, 0.0))
"""One unit step in the negative Y direction."""

RIGHT = np.array((1.0, 0.0, 0.0))
"""One unit step in the positive X direction."""

LEFT = np.array((-1.0, 0.0, 0.0))
"""One unit step in the negative X direction."""

IN = np.array((0.0, 0.0, -1.0))
"""One unit step in the negative Z direction."""

OUT = np.array((0.0, 0.0, 1.0))
"""One unit step in the positive Z direction."""

# Geometry: axes
X_AXIS = np.array((1.0, 0.0, 0.0))
Y_AXIS = np.array((0.0, 1.0, 0.0))
Z_AXIS = np.array((0.0, 0.0, 1.0))

# Geometry: useful abbreviations for diagonals
UL = UP + LEFT
"""One step up plus one step left."""

UR = UP + RIGHT
"""One step up plus one step right."""

DL = DOWN + LEFT
"""One step down plus one step left."""

DR = DOWN + RIGHT
"""One step down plus one step right."""

# Geometry
START_X = 30
START_Y = 20

# Default buffers (padding)
SMALL_BUFF = 0.1
MED_SMALL_BUFF = 0.25
MED_LARGE_BUFF = 0.5
LARGE_BUFF = 1
DEFAULT_MOBJECT_TO_EDGE_BUFFER = MED_LARGE_BUFF
DEFAULT_MOBJECT_TO_MOBJECT_BUFFER = MED_SMALL_BUFF

# Times in seconds
DEFAULT_POINTWISE_FUNCTION_RUN_TIME = 3.0
DEFAULT_WAIT_TIME = 1.0

# Misc
DEFAULT_POINT_DENSITY_2D = 25
DEFAULT_POINT_DENSITY_1D = 250
DEFAULT_STROKE_WIDTH = 4

# Mathematical constants
PI = np.pi
"""The ratio of the circumference of a circle to its diameter."""

TAU = 2 * PI
"""The ratio of the circumference of a circle to its radius."""

DEGREES = TAU / 360
"""The exchange rate between radians and degrees."""

# ffmpeg stuff
FFMPEG_BIN = "ffmpeg"

# gif stuff
GIF_FILE_EXTENSION = ".gif"

# Colors
COLOR_MAP = {
    "WHITE": "#EBF2FA",
    "GRAY_DARKER": "#C5CDD6",
    "GRAY_DARK": "#9EA8B1",
    "GRAY": "#78848D",
    "GRAY_LIGHT": "#515F68",
    "GRAY_LIGHTER": "#2B3A44",
    "BLACK": "#04151F",
    "YELLOW_LIGHTER": "#e2cc92",
    "YELLOW_LIGHT": "#d8bb6e",
    "YELLOW": "#ceaa4a",
    "YELLOW_DARK": "#a5883b",
    "YELLOW_DARKER": "#7c662c",
    "ORANGE_LIGHTER": "#e2b293",
    "ORANGE_LIGHT": "#d8996f",
    "ORANGE": "#CE7F4B",
    "ORANGE_DARK": "#a5663c",
    "ORANGE_DARKER": "#7c4c2d",
    "RED_LIGHTER": "#e29893",
    "RED_LIGHT": "#d8756f",
    "RED": "#ce534b",
    "RED_DARK": "#a5423c",
    "RED_DARKER": "#7c322d",
    "BLUE_LIGHTER": "#8eafc7",
    "BLUE_LIGHT": "#6895b4",
    "BLUE": "#427AA1",
    "BLUE_DARK": "#356281",
    "BLUE_DARKER": "#284961"
}
COLOR_MAP.update(
    {
        name.replace("_C", ""): COLOR_MAP[name]
        for name in COLOR_MAP
        if name.endswith("_C")
    }
)
PALETTE = list(COLOR_MAP.values())
locals().update(COLOR_MAP)
FFMPEG_VERBOSITY_MAP = {
    "DEBUG": "error",
    "INFO": "error",
    "WARNING": "error",
    "ERROR": "error",
    "CRITICAL": "fatal",
}
VERBOSITY_CHOICES = FFMPEG_VERBOSITY_MAP.keys()
