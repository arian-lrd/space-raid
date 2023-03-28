import pygame
from pygame.sprite import Sprite
import random


class AlienBullet(Sprite):
    """A class to manage bullets fired from the aliens."""

    def __init__(self, ai_settings, screen, aliens, ship):
        """Create a bullet at an aliens current position."""
        super().__init__()
        self.screen = screen

        self.all_alien_rects = []
        for alien in aliens:
            self.all_alien_rects.append(alien.rect)
        self.random_alien_rect = random.choice(self.all_alien_rects)

        # Create a bullet at (0, 0) and then set its position.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
                                ai_settings.bullet_height)


        self.rect.centerx = self.random_alien_rect.centerx
        self.rect.centery = self.random_alien_rect.centery + 10

        # Store the alien_bullet's y position as a decimal value
        self.y = float(self.rect.centery)

        self.color = ai_settings.alien_bullet_color
        self.speed_factor = ai_settings.alien_bullet_speed_factor

    def update(self):
        """Move the alien bullet down the screen."""
        # Update the decimal position of the bullet
        self.y += self.speed_factor
        # Update the rect position
        self.rect.centery = self.y

    def draw_alien_bullet(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)
