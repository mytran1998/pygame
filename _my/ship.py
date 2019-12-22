import pygame
class Ship:
    """ A class to manage the ship """
    def __init__(self, screen):
        """ Initiliazing the ship and set its starting position"""
        self.screen = screen

        # Load image 
        self.image = pygame.image.load('images/airplane.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Khoi tao vi tri bat dau
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Direction
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """ Draw the ship at its current location """
        self.screen.blit(self.image, self.rect)

    def update(self):
        """ Update the ship's position based on direction."""
        if self.moving_right:
            self.rect.centerx += 5
        if self.moving_left:
            self.rect.centerx -= 5
        """ Kiểm tra không cho tràn viền"""
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
        
