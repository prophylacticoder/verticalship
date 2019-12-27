import pygame
import sys
from bullet import Bullet

def check_events(ai_settings, screen, ship, bullets):
    """Watch for keyboard and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    if event.key == pygame.K_UP:
        ship.moving_up = True
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    elif event.key == pygame.K_SPACE:
        # Create a new bullet and add to the bullets group
        fire_bullets(ai_settings, screen, ship, bullets)

def check_keyup_events(event, ship):
    if event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_settings, screen, ship, bullets):
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    for bullet in bullets.sprites():
        bullet.draw_bullet()
 # Make the most recently drawn screen visible.
    pygame.display.flip()

def update_bullets(bullets, screen):
    bullets.update()
    screen_rect = screen.get_rect()
    for bullet in bullets.copy():
        if bullet.rect.left >= screen_rect.right:
            bullets.remove(bullet)
def fire_bullets(ai_settings, screen, ship, bullets):
    if len(bullets) < 3:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
