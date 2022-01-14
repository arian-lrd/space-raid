import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Store and visualize the ship."""

    def __init__(self, ai_settings, screen):
        """Initialize the ship and its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load ship image and get its rect
        self.image = pygame.image.load('images/index_adobespark2.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store a decimal value for the ship's center
        self.center = float(self.rect.centerx)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update(self):
        """Update the ships position based on the flags."""
        # Update the ship's center value, not the rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        # Update rect object from self.center.
        self.rect.centerx = self.center

    def center_ship(self):
        self.center = self.screen_rect.centerx

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
        # Fekr konm, self.screen e qable blit yani mikhaim rooye oon ye chize dge bbarim
        # va self.image e too parantez oon chizie ke mikhaim bebarimesh roo ye chize dge


# FUN
class Masamune():
    """Store and visualize Masamune."""
    def __init__(self, screen):
        """Initialize Masamune and his starting position"""
        self.screen = screen

        # Load Masamune and get his rec
        self.image = pygame.image.load('images/DurrrSpaceShip_resized.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = self.screen.get_rect()

        # Put Masamune in the middle of the screen
        self.rect.center = self.screen_rect.center

    def blitme(self):
        """Draw masamune on his location"""
        self.screen.blit(self.image, self.rect)
