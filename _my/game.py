import sys
import pygame
from ship import Ship
from bullet import Bullet
from alien import Alien
from pygame.sprite import Sprite
import game_event
import random

WIDTH = 500
HEIGHT = 600
FPS = 60
BACKGROUND_COLOR = (230, 230, 230) 
clock = pygame.time.Clock()

class Game:
    """ Overall class to manage game assets and behavior."""
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        self.image = pygame.image.load('images/background.png')
        self.rect = self.image.get_rect()
        # Tạo con tàu
        self.ship = Ship(self.screen)
        # Tạo nhóm để lưu trữ bullet
        self.bullets = pygame.sprite.Group()
        # Tạo nhóm để lưu trữ alien
        self.aliens = pygame.sprite.Group()
        # Tính điểm
        self.score = 0
    def run_game(self):
        """ Main loop for the game."""
        # Tạo 5 alien
        game_event.create_alien(self.screen, self.aliens, 5)
        while True:
            clock.tick(FPS)
            self.check_event()
            # Change the ship's position by calling its 'update' method
            self.ship.update()

            # Update every bullet on the screen
            game_event.update_and_delete_bullet(self, self.bullets)

            # Update every alien on the screen 
            self.aliens.update()

            # Kiem tra neu Aline cham vao Bullet
            game_event.check_coll_bullet_alien(self, self.aliens, self.bullets, self.screen)

            # Kiem tra neu Alien va cham ship
            check = game_event.check_coll_alien_ship( self.ship, self.aliens)
            if check:
                game_event.draw_game_over(self.screen)
                stop = True
                while stop:
                    clock.tick(FPS)
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            sys.exit()
                        elif event.type == pygame.KEYDOWN:
                            self.score = 0
                            game_event.create_alien(self.screen, self.aliens, 1)
                            stop = False

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
        # Draw list of bullets
        game_event.draw_bullet(self.bullets)
        # Draw list of aliens
        game_event.draw_aline(self.aliens)
        # Hien thi diem 
        game_event.draw_score(self.screen, 'Score : {}'.format(str(self.score)), 25, WIDTH/2, 10)
        # Make the most recently drawn screen visible.
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    game = Game()
    game.run_game()
