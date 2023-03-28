import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen

        # Load the alien image and set its rect attribute
        self.image_initial = pygame.image.load('images/alien-copy_adobespark.png')
        self.image = pygame.transform.scale(self.image_initial, self.ai_settings.space_craft_scale)
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alien's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien at its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        self.screen_rect = self.screen.get_rect()
        if self.rect.right >= self.screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Move the alien to the right."""
        self.x += (self.ai_settings.alien_speed_factor *
                   self.ai_settings.fleet_direction)
        self.rect.x = self.x
