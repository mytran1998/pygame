import pygame

class ShipMini:
	def __init__(self, screen, x, y, quantity):
		self.screen = screen
		self.image = pygame.image.load('images/ship-mini.png')
		self.rect = self.image.get_rect()
		self.rect.x = x + 30 * quantity
		self.rect.y = y
	def blitme(self):
		self.screen.blit(self.image, self.rect)