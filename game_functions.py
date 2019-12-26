import pygame

def update_screen(screen, vs_settings, ship):
  screen.fill(vs_settings.bg_color)
  ship.blitme()
  pygame.display.flip()
