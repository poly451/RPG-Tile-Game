# From:
# https://github.com/kidscancode/pygame_tutorials/blob/master/tilemap/part%2001/settings.py
# ===========================================================
# define some colors (R, G, B)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARKGREY = (40, 40, 40)
LIGHTGREY = (100, 100, 100)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

UP = 90
DOWN = -90
RIGHT = 0
LEFT = 180

# game settings
WIDTH = 1024   # 16 * 64 or 32 * 32 or 64 * 16
HEIGHT = 768  # 16 * 48 or 32 * 24 or 64 * 12
FPS = 60
TITLE = "PLAYER ORIENTATION"
BGCOLOR = DARKGREY

TILESIZE = 64 # 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE

# player settings
PLAYER_ROT_SPEED = 250
PLAYER_IMG = 'manBlue_gun.png'
