import pygame

class Ship():
    """Class that has the data of the ship."""
    def __init__(self, ai_settings, screen):
        self.screen = screen

        self.ai_settings = ai_settings

        # Load ship's image and get its rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start the new ship on the bottom center of the screen
        self.rect.centery = self.screen_rect.centery

        # Atrribute that will finer speed adjustment of the ship
        self.center = float(self.rect.centery)

        # Flag that sets the motion to the right
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the ship on the screen in the rect position."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_up and self.rect.top > self.screen_rect.top:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom <= self.screen_rect.bottom:
            self.center += self.ai_settings.ship_speed_factor
        # Update rect object from self.center
        self.rect.centery = self.center
