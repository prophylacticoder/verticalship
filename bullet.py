import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_settings, screen, ship):
        '''Create a bullet object at its current ship's position.'''
        super().__init__()
        self.screen = screen

        # Create the bullet's rectangle and set its correct position
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.right
        self.rect.centery = ship.rect.centery

        # Store the bullets' position as a decimal value
        self.x = float(self.rect.x)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        '''Update the position of the bullet.'''
        self.x += self.speed_factor
        # Update the rect position
        self.rect.x = self.x

    def draw_bullet(self):
        '''Draw the bullet on the screen.'''
        pygame.draw.rect(self.screen, self.color, self.rect)
