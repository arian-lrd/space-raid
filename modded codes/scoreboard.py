import pygame.font
from pygame.sprite import Group

from ship import Ship

class Scoreboard():
    """A class to report scoring information."""

    def __init__(self, ai_settings, screen, stats):
        """Initialize score keeping attributes."""
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        # Font settings for scoring information.
        self.text_color = (255, 255, 255)
        self.font_highscore = pygame.font.Font('fonts/space_invaders copy.ttf', 35)
        self.font_lvl = pygame.font.Font(
            'fonts/space_invaders copy.ttf', 20)
        self.font_score = pygame.font.Font(
            'fonts/space_invaders copy.ttf', 30)

        self.prep_images()

    def prep_score(self):
        """Turn the score into a rendered image."""
        rounded_score = round(self.stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font_score.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # Display the score at the top right of the screen.
        self.score_image_rect = self.score_image.get_rect()
        self.score_image_rect.right = self.screen_rect.right - 20
        self.score_image_rect.top = 20

    def show_score(self):  # TODO: update the definition
        """Draw level, score and high score to the screen."""
        self.screen.blit(self.score_image, self.score_image_rect)
        self.screen.blit(self.high_score_image, self.high_score_image_rect)
        self.screen.blit(self.level_image, self.level_image_rect)
        # Draw ships.
        self.ships.draw(self.screen)

    def prep_high_score(self):
        """Turn the high score into a rendered image."""
        rounded_high_score = round(self.stats.high_score, -1)
        high_score_str = "High score " + "{:,}".format(rounded_high_score)
        self.high_score_image = self.font_highscore.render(
            high_score_str, True, self.text_color, self.ai_settings.bg_color)

        # Center the high score at the top of the screen.
        self.high_score_image_rect = self.high_score_image.get_rect()
        self.high_score_image_rect.centerx = self.screen_rect.centerx
        self.high_score_image_rect.top = self.screen_rect.top

    def prep_level(self):
        """Turn level into a rendered image."""
        level_str = "Lvl:" + str(self.stats.level)
        self.level_image = self.font_lvl.render(
            level_str, True, self.text_color,
            self.ai_settings.bg_color
        )

        # Position the level below the score
        self.level_image_rect = self.level_image.get_rect()
        self.level_image_rect.right = self.score_image_rect.right
        self.level_image_rect.top = self.score_image_rect.bottom + 10

    def prep_ships(self):
        """Show how many ships are left."""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)
            ship.rect.x = 10 + ((ship.rect.width - 40) * ship_number )
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_images(self):
        """Prepare the initial score,
         high score, level and extra ships images."""
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()
