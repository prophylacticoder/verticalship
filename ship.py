import pygame

class Ship():
  '''Necessary ship configuration to be drawn on the screen.'''
  def __init__(self, screen):
      self.screen = screen

      self.image = pygame.image.load('images/ship.bmp')
      self.rect = self.image.get_rect()
      self.screen_rect = self.screen.get_rect()
      # Center the ship within the Y-axis
      self.rect.centery = self.screen_rect.centery


  def blitme(self):
      self.screen.blit(self.image, self.rect)
