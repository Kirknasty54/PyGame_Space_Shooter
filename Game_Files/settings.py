import pygame as pg
import os
import random

FPS = 60
level = 0
lives = 5
difficulty = FPS
main_font = pg.font.SysFont("franklingothicmedium", 50)
lost_font = pg.font.SysFont("couriernew", 50)
player_vel = 10
laser_vel = 5
lost_count = 0
enemies = []
wave_length = 5
enemy_vel = 1
pg.display.set_caption("Space Invaders")
monitor_size = pg.display.Info()
screen_width, screen_height = monitor_size.current_w, monitor_size.current_h
WIN = pg.display.set_mode((screen_width-10, screen_height-50), pg.RESIZABLE)
surface = pg.Surface((screen_width, screen_height), pg.SRCALPHA)
BG = pg.transform.scale(pg.image.load(os.path.join("../assets", "background-black.png")).convert_alpha(), (WIN.get_width(), WIN.get_height()))
BG1 = pg.transform.scale(pg.image.load(os.path.join("../assets", "main_menu_screen.png")).convert_alpha(), (WIN.get_width(), WIN.get_height()))
clock = pg.time.Clock()
fullscreen = False
lost_messages = ["Wow, you lost at this?",
                     "My grandma can play better than you!",
                     "You lost!",
                     "This the best you got?",
                     "You need more power kiddo"]
lost_label = lost_font.render(lost_messages[random.randrange(0, len(lost_messages) - 1)], 1, (255, 255, 255))