from ship import *
from settings import *

#enemy ships and lasers
RED_SPACE_SHIP = pg.image.load(os.path.join("../assets", "pixel_ship_red_small.png")).convert_alpha()
GREEN_SPACE_SHIP = pg.image.load(os.path.join("../assets", "pixel_ship_green_small.png")).convert_alpha()
BLUE_SPACE_SHIP = pg.image.load(os.path.join("../assets", "pixel_ship_blue_small.png")).convert_alpha()
RED_LASER = pg.image.load(os.path.join("../assets", "pixel_laser_red.png")).convert_alpha()
GREEN_LASER = pg.image.load(os.path.join("../assets", "pixel_laser_green.png")).convert_alpha()
BLUE_LASER = pg.image.load(os.path.join("../assets", "pixel_laser_blue.png")).convert_alpha()

class Enemy(Ship):
    COLOR_MAP = {
        "red": (RED_SPACE_SHIP, RED_LASER),
        "green": (GREEN_SPACE_SHIP, BLUE_LASER),
        "blue": (BLUE_SPACE_SHIP, BLUE_LASER)
    }


    def __init__(self, x, y, color, health=100):
        super().__init__(x, y, health)
        self.ship_img, self.laser_img = self.COLOR_MAP[color]
        self.mask = pg.mask.from_surface(self.ship_img)

    def move(self, vel):
        if not Ship.pause:
            self.y += vel