import pygame
from pygame.sprite import Sprite


class Power(Sprite):
    def __init__(self, center, screen):
        super(Power, self).__init__()
        self.screen = screen
        self.image = pygame.image.load('images/heart.png')
        self.rect = self.image.get_rect()
        #self.rect = pygame.Rect(0, 0, 5, 30)
        self.rect.center = center

        self.speed_y = 2
		
    def blitme(self):
        #pygame.draw.rect(self.screen, self.color, self.rect)
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > 600:
            self.kill()