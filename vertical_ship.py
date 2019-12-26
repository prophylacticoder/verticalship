import pygame
import sys
import settings
from ship import Ship
import game_functions as gf

def run_game():
  pygame.init()

  vs_settings = settings.Vs_Settings()
  screen = pygame.display.set_mode((vs_settings.window_width, vs_settings.window_height))
  pygame.display.set_caption('Vertical Shipping')

  ship = Ship(screen)

  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          sys.exit()
    gf.update_screen(screen, vs_settings, ship)

run_game()
