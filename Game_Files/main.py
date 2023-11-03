import pygame as pg, sys
print("this should auto update")
pg.init()
import time
from pygame.locals import *
from enemy_character import *
from player_character import *
from settings import *
from button import *
pg.font.init()
import random

def get_font(size):
    return pg.font.Font(os.path.join("../assets", "font.ttf"))

class Game:
    def __init__(self):
        pg.init()
        self.player = Player(300, 650, False)
        self.clock = clock
        self.lost = False
        self.lost_count = lost_count
        self.level = level
        self.wave_length = wave_length
        self.lives = lives
        self.player_vel = player_vel
        self.runCheck = True
        self.level = level
        self.lives = lives
        self.main_font = main_font
        self.lost_font = lost_font
        self.player_vel = player_vel
        self.laser_vel = laser_vel
        self.lost_count = lost_count
        self.enemies = enemies
        self.wave_length = wave_length
        self.difficulty = difficulty

    #this creates the main menu and is where we can click on buttons to either play the game or
    def main_menu(self):
        while True:
            WIN.blit(BG1, (0, 0))
            MENU_MOUSE_POS = pg.mouse.get_pos()
            MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
            MENU_RECT = MENU_TEXT.get_rect(center=(WIN.get_width()/2, WIN.get_height()/2-300))

            PLAY_BUTTON = Button(image=pg.image.load(os.path.join("../assets", "play_rect.png")), pos=(WIN.get_width()/2, WIN.get_height()/2-150),
                                 text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
            QUIT_BUTTON = Button(image=pg.image.load(os.path.join("../assets", "play_rect.png")), pos=(WIN.get_width()/2, WIN.get_height()/2),
                                 text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

            WIN.blit(MENU_TEXT, MENU_RECT)

            for button in [PLAY_BUTTON, QUIT_BUTTON]:
                button.changeColor(MENU_MOUSE_POS)
                button.update(WIN)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == pg.MOUSEBUTTONDOWN:
                    if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                        self.run()
                    if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                        pg.quit()
                        sys.exit()
            pg.display.update()

    def draw_pause(self):
        pg.draw.rect(surface, (128, 128, 128, 150), [0, 0, screen_width, screen_height])
        WIN.blit(surface, (0, 0))
        pg.display.update()

    def redraw_window(self):
        WIN.fill("black")
        #takes one of the pg images that have been turned into a surface and draws it at the location we have indicated
        WIN.blit(BG, (0,0))
        #draw text
        lives_label = main_font.render(f"x{self.lives}", 1, (255, 255, 255))
        level_label = main_font.render(f"Level: {self.level}", 1, (255, 255, 255))

        WIN.blit(self.player.ship_img, (10, 10)), WIN.blit(lives_label, (screen_width + (-screen_width + 120), screen_height + (-screen_height + 35)))
        WIN.blit(level_label, (WIN.get_width() - level_label.get_width() - 10, 10))

        for enemy in enemies:
            enemy.draw(WIN)

        self.player.draw(WIN)

        if self.lost:
            WIN.blit(lost_label, (WIN.get_width()/2 - lost_label.get_width()/2, 350))

        pg.display.update()

    def run(self):
        while self.runCheck == True:
            #clock will be ticked based on FPS, makes sure game stay consistent on any device
            clock.tick(FPS)
            self.player.movement()
            self.redraw_window()
            if self.lives <= 0 or self.player.health <= 0:
                self.lost = True
                self.lost_count += 1

            messageOcurrance = 0
            if self.lost:
                if self.lost_count > FPS * 3:
                    self.runCheck = False
                else:
                    continue

            #if no enemies are left, increment level, increment num of enimes
            if len(enemies) == 0:
                self.level += 1
                self.difficulty *= 0.9
                self.wave_length += 5
                for i in range(self.wave_length):
                    enemy = Enemy(random.randrange(50, WIN.get_width()-100), random.randrange(-1500 * ((self.level+1) // 2), -100), random.choice(["red", "blue", "green"]))
                    enemies.append(enemy)

            keys = pg.key.get_pressed()

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    run = False

                #figure this bullshit out later
                '''if event.type == VIDEORESIZE:
                    pass #WIN = pg.display.set_mode((event.w, event. h), pg.RESIZABLE)'''
                if keys[pg.K_ESCAPE]:
                    if Ship.pause:
                        Ship.pause = False
                    else:
                        Ship.pause = True
                        self.draw_pause()
                        print("the game is now pauses")
                    #pg.quit()
                    #sys.exit()
                '''if keys[pg.K_f]:
                    fullscreen = not fullscreen
                    if fullscreen:
                        pass#WIN = pg.display.set_mode(monitor_size, pg.FULLSCREEN)
                    else:
                        pass#WIN = pg.display.set_mode((WIN.get_width(), WIN.get_height()), pg.FULLSCREEN)'''

            for enemy in enemies[:]:
                enemy.move(enemy_vel)
                enemy.move_lasers(laser_vel, self.player)

                if random.randrange(0, round((FPS * 2) * self.difficulty)) < 30:
                    enemy.shoot()

                if enemy.collide(self.player):
                    self.player.health -= 10
                    enemies.remove(enemy)
                elif enemy.y + enemy.get_height() > WIN.get_height():
                    print("Successuly lost life")
                    self.lives -= 1
                    enemies.remove(enemy)

            self.player.move_lasers(-laser_vel, enemies)

if __name__ == '__main__':
    game = Game()
    game.main_menu()
    #game.run()