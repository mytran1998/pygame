import sys
import pygame, os
from os import path
from ship import Ship
from bullet import Bullet
from alien import Alien
from explosions import Explosion
from pygame.sprite import Sprite
import game_event
import random
from pygame.locals import *

WIDTH = 500
HEIGHT = 600
FPS = 60
LIVES = 3
WHITE = (255,255,255)
YELLOW = (255,255,0)
clock = pygame.time.Clock()
# Set vị trí bắt đầu khi khởi động
pos_x = 1360 / 2 - WIDTH / 2
pos_y = 760 - HEIGHT
os.environ['SDL_VIDEO_WINDOW_POS'] = '%i,%i' % (pos_x,pos_y)
os.environ['SDL_VIDEO_CENTERED'] = '0'
#Nhạc nền
music_dir = path.join(path.dirname(__file__), 'music')
pygame.mixer.init()
pygame.mixer.music.load(path.join(music_dir, 'a song.ogg'))
pygame.mixer.music.play(loops=-1)

class Game:
    """ Overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()
        pygame.mixer.init()
        pygame.display.set_caption(u'SHOT PLANE')
        pygame.display.set_icon(pygame.image.load("images/icon.png"))
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()
        # Tạo con tàu
        self.ship = Ship(self.screen)
        # Tạo nhóm để lưu trữ bullet
        self.bullets = pygame.sprite.Group()
        # Tạo nhóm để lưu trữ alien
        self.aliens = pygame.sprite.Group()
        # Hiệu ứng nổ
        self.explosions = pygame.sprite.Group()
        # Power
        self.powers = pygame.sprite.Group()
        # Tính điểm
        self.score = 0
    def run_game(self):
        """ Main loop for the game."""
        # Tạo 5 alien
        game_event.create_alien(self.screen, self.aliens, 10)
        while True:
            clock.tick(FPS)
            self.check_event()
            # Change the ship's position by calling its 'update' method
            self.ship.update()

            # Update every bullet on the screen
            game_event.update_and_delete_bullet(self, self.bullets)

            # Update every alien on the screen 
            self.aliens.update()

            # Update Expl
            self.explosions.update()

            # Update Power
            self.powers.update()

            # Kiem tra neu Aline cham vao Bullet
            game_event.check_coll_bullet_alien(self, self.aliens, self.bullets, 
                self.screen, self.explosions, self.powers)
            # Kiem tra neu Ship cham vao Power
            game_event.check_coll_ship_power(self.ship, self.powers)
            
            # Kiem tra neu Alien va cham ship
            check = game_event.check_coll_alien_ship( self.ship, self.aliens, self.screen, self.explosions)
            if check:
                stop = True
                game_event.draw_game_over(self.screen, self)
                pygame.display.flip()
                pygame.mixer.music.stop()
                while stop:
                    clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == K_ESCAPE:
                                sys.exit()
                            elif event.key == K_SPACE:
                                stop = False
                            
                self.score = 0
                self.ship.shield = 100
                self.ship.lives = LIVES
                pygame.mixer.music.play()
                game_event.create_alien(self.screen, self.aliens, 1)
            self.update_game()

    def check_event(self):
        """ Watch for keyboard and mouse event."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            # Check key pressed
            elif event.type == pygame.KEYDOWN:
                game_event.event_keydown(event, self, self.ship, self.screen , self.bullets)
            # Check key released
            elif event.type == pygame.KEYUP:
                game_event.event_keyup(event, self.ship)

    def update_game(self):
        # Redraw the screen
        self.screen.blit(self.image, self.rect)
        # Draw the ship
        self.ship.blitme()
        # Draw list of Explosions
        game_event.draw_expl(self.explosions)
        # Draw list of bullets
        game_event.draw_bullet(self.bullets)
        # Draw list of aliens
        game_event.draw_aline(self.aliens)
        # Draw list of powers
        game_event.draw_power(self.powers)
        # Hien thi diem 
        game_event.draw_score(self.screen, 'SCORE : {}'.format(str(self.score)), 25, WIDTH/2, 10, YELLOW)
        #Hien thi % mau
        game_event.draw_shield(5, 5, self.screen, self.ship.shield)
        # Số mạng
        game_event.draw_ship_mini(self.screen, WIDTH - 100, 10, self.ship.lives)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game_event.draw_menu_start(game.screen, game)
    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                done = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game.run_game()
    
