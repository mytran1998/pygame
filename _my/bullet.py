import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/bullet.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        #self.rect = pygame.Rect(0, 0, 5, 30)
        self.rect.centerx = ship.rect.centerx
        self.rect.bottom = ship.rect.bottom

        #self.color = (250, 0, 0)
		
    def draw_bullet(self):
        #pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)

    def update(self, game):
        if self.rect.bottom > 0:
            self.rect.y -= 10
		
		
