

class Constants:
    counterUntilFrame = 0  # count up until table is fixed
    LEFT = 0
    RIGHT = 1
    X_COORDINATE = 0
    Y_COORDINATE = 1
    EPSILON = 40
    LAST = -1
    FPS = 30
    Ball_ID_NEW_TRAIN = 0
    Hand_ID_NEW_TRAIN = 1
    NET_ID = 1
    TABLE_ID = 2
    L_RESULT = 5
    R_RESULT = 0
    THRESHOLD = 0.15  # threshold of accuracy of classification
    TABLE_SIZE = 1
    LEFT_PLAYER = 0
    RIGHT_PLAYER = 1
    NET_X = 0

    ALLOWED_MISTAKES = 6
    FRAMES_TO_COUNT = 15

    wait_hand = 0
    wait_for_fault = 1
    WON_REASON = "NONE"


class Dimensions:
    TABLE_WIDTH = 152.5
    TABLE_HEIGHT = 76
    TABLE_HALF_LENGTH = 137  # ALL TABLE LENGTH IS 137*2
    OFFICIAL_TABLE_TENNIS_LENGTH = 274
    cm_per_seconds_to_km_per_hour = 0.036
    max_allowed_speed = 150


# colors defined in BGR format: this is how open cv work with colors
class Color:
    BLACK = (0, 0, 0)
    RED = (0, 0, 255)
    GREEN = (0, 255, 0)
    BLUE = (255, 0, 0)
    PURPLE = (128, 0, 128)
    MAGENTA = (255, 0, 255)
    YELLOW = (0, 255, 255)
    WHITE = (255, 255, 255)
    PINK = (203, 192, 255)  # Adjusted to a lighter shade of pink
    AQUA = (255, 255, 0)
    ORANGE = (0, 165, 255)
    BROWN = (42, 42, 165)
    MAROON = (0, 0, 128)
    TEAL = (128, 128, 0)
    NAVY = (128, 0, 0)
    OLIVE = (0, 128, 128)
    LIME = (0, 255, 0)
    CYAN = (255, 255, 0)
    SILVER = (192, 192, 192)
    GRAY = (128, 128, 128)
    DARK_GRAY = (64, 64, 64)
    LIGHT_GRAY = (192, 192, 192)
    GOLD = (0, 215, 255)
    SALMON = (114, 128, 250)
    TURQUOISE = (208, 224, 64)
    INDIGO = (130, 0, 75)
    STEEL_BLUE = (180, 130, 70)
    TAN = (140, 180, 210)
    VIOLET = (238, 130, 238)
