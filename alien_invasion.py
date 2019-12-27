import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
 # Initialize game and create a screen object.
 pygame.init()
 ai_settings = Settings()
 screen = pygame.display.set_mode((ai_settings.window_width, ai_settings.window_height))
 pygame.display.set_caption("Alien Invasion")

 # Make a Ship
 ship = Ship(ai_settings, screen)

 bullets = Group()

 # Start the main loop for the game.
 while True:
 # Watch for keyboard and mouse events.
    gf.check_events(ai_settings, screen, ship, bullets)
    ship.update()
    gf.update_bullets(bullets, screen)
    gf.update_screen(ai_settings, screen, ship, bullets)

run_game()
