import pygame
import random
from  pygame.sprite import Sprite

alien_list = ['images/big1.png', 'images/big2.png', 'images/med3.png',
			 'images/small1.png', 'images/small2.png', 'images/med1.png']

class Alien(Sprite):
	def __init__(self, screen):
		super(Alien, self).__init__()
		self.screen = screen

		# Load image 
		self.image = pygame.image.load(alien_list[random.randint(0, len(alien_list) - 1)])
		self.rect = self.image.get_rect()

		# Tao vi tri ran dom
		self.rect.x = random.randrange(500 - self.rect.width)
		self.rect.y = random.randrange(-100, -50)

		# Lưu vị trí chính xác
		self.x = float(self.rect.x)

		self.speed_x = random.randrange(-3, 3)
		self.speed_y = random.randrange(1, 8)

	def blitme(self):
		# Vẽ vị trí alien hiện tại
		self.screen.blit(self.image, self.rect)

	def update(self):
		self.rect.x += self.speed_x
		self.rect.y += self.speed_y
		if self.rect.top > 600 or self.rect.left < -25 or self.rect.right > 500:
			self.rect.x = random.randrange(500 - self.rect.width)
			self.rect.y = random.randrange(-100, -50)
			self.speedy = random.randrange(1, 8)