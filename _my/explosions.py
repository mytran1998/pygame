import pygame, os
from os import path
from pygame.sprite import Sprite

BLACK = (0, 0, 0)
bum_img = ['images/bum01.png','images/bum02.png','images/bum03.png']

# Hiệu ứng khi va chạm
class Explosion(Sprite):
	def __init__(self, center, screen, quantity):
		pygame.sprite.Sprite.__init__(self)
		self.screen = screen
		self.image = pygame.image.load(bum_img[quantity])
		self.rect = self.image.get_rect()
		#self.screen_rect = screen.get_rect()
		self.rect.center = center

	def blitme(self):
		self.screen.blit(self.image, self.rect)