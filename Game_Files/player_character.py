from ship import *
from settings import *

#player's ship
YELLOW_SPACE_SHIP = pg.image.load(os.path.join("../assets", "pixel_ship_yellow.png")).convert_alpha()
YELLOW_LASER = pg.image.load(os.path.join("../assets", "pixel_laser_yellow.png")).convert_alpha()

class Player(Ship):
    def __init__(self,x, y, pause, health = 100):
        super().__init__(x, y , health)
        self.ship_img = YELLOW_SPACE_SHIP
        self.laser_img = YELLOW_LASER
        self.mask = pg.mask.from_surface(self.ship_img)
        self.max_health = health
        self.player_vel = player_vel


    def movement(self):
        keys = pg.key.get_pressed()
        if not Ship.pause:
            if (keys[pg.K_a] or keys[pg.K_LEFT]) and self.x - self.player_vel > 0:  # moving left
                self.x -= self.player_vel
            if (keys[pg.K_d] or keys[
                pg.K_RIGHT]) and self.x + self.player_vel + self.get_width() < WIN.get_width():  # moving right
                self.x += self.player_vel
            if (keys[pg.K_w] or keys[pg.K_UP]) and self.y - self.player_vel > 0:  # moving up
                self.y -= self.player_vel
            if (keys[pg.K_s] or keys[
                pg.K_DOWN]) and self.y + self.player_vel + self.get_height() < WIN.get_height():  # moving down
                self.y += self.player_vel

            if keys[pg.K_SPACE]:
                self.shoot()

    def move_lasers(self, vel, objs):
        self.cooldown()
        if not self.pause:
            for laser in self.lasers:
                laser.move(vel)
                if laser.off_screen(WIN.get_height()):
                    self.lasers.remove(laser)
                    print("laser successfuly remove")
                else:
                    for obj in objs:
                        if laser.collision(obj):
                            objs.remove(obj)
                            if laser in self.lasers:
                                self.lasers.remove(laser)

    def draw(self, window):
        super().draw(window)
        self.health_bar(window)

    def health_bar(self, window):
        pg.draw.rect(window, (255, 0, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pg.draw.rect(window, (0, 255, 0), (self.x, self.y + self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health / self.max_health), 10))