import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group
from game_stats import Gamestats
from button import Button
from scoreboard import Scoreboard
from sound_and_music import Sounds


def run_game():
    """Initialize game, settings, and screen object."""
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()
    ai_settings = Settings()
    # Make a Sounds instance after the Settings instance
    ai_sounds = Sounds(ai_settings)


    screen = pygame.display.set_mode((
        ai_settings.screen_width, ai_settings.screen_height), pygame.RESIZABLE)
    pygame.display.set_caption("Alien Invasion")

    # PLay the menu music
    ai_sounds.play_menu_music()

    # Make the play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statics and create a scoreboard.
    stats = Gamestats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    explosions = Group()
    alien_bullets = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings, screen, ship, aliens)


    # Start the main loop of the program
    while True:
        # Watch for keyboard and mouse events
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship,
                        aliens, bullets, ai_sounds, explosions, alien_bullets)
        if stats.game_active:
            ai_sounds.check_for_new_background_song()
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens,
                              bullets, ai_sounds, explosions, alien_bullets, play_button)
            gf.update_explosions(explosions)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens,
                             bullets, ai_sounds, explosions, play_button, alien_bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets,
                         play_button, explosions, alien_bullets) # TODO: inja draw explosions darim



run_game()
