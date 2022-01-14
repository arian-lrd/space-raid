import pygame

class Settings():
    """A class to store all settings for alien invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (7, 9, 22)
        self.bg_image_raw = pygame.image.load('images/possible background image.jpg')
        self.bg_image_done = pygame.transform.scale(self.bg_image_raw, (1200, 800))

        # ship settings
        self.ship_limit = 3  # player actually has 4 tries

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 255, 231, 181
        self.bullets_allowed = 4
        # Alien bullets
        self.alien_bullet_width = 3
        self.alien_bullet_height = 15
        self.alien_bullet_color = 0, 173, 255
        self.alien_bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        # Music and sound settings and volumes
        # Files
        self.background_music_files = []
        self.background_music_files.append('music/background_music'
                                           '/Arcade - Public Memory.wav')
        self.background_music_files.append('music/background_music'
                                           '/Project - Patrick Patrikios.wav')
        self.background_music_files.append('music/background_music'
                                           '/19th Floor - Bobby Richards.wav')
        self.background_music_files.append('music/background_music'
                                           '/Tak - Bobby Richards.wav')
        self.background_music_files.append('music/background_music'
                                           '/Brass Orchid - Bobby Richards.wav')
        self.background_music_files.append('music/background_music'
                                           '/Average - Patrick Patrikios.wav')

        self.background_music_volume = 0.1
        self.current_song_index = 0
        self.total_song_number = 6

        self.menu_music_file = 'music/space_menu.wav'
        self.laser_sound_file = 'music/Project 1 - 9_7_1400 AP, 18.54.wav'
        self.alien_explosion_sound_file = 'music/explosion.wav'
        self.ship_explosion_sound_file = 'music/ship_explosion.wav'
        self.alien_reach_bottom_sound_file = 'music/fast-game-over-version2.wav'
        self.gameover_sound_file = 'music/mixkit-spaceship-system-break-down-2959.wav'

        # Volumes and other settings

        self.background_music_volume = 0.2
        self.menu_music_volume = 0.5
        self.laser_sound_volume = 0.1
        self.explosion_sound_volume = 0.1
        self.ship_explosion_sound_volume = 0.4
        self.alien_reach_bottom_sound_volume = 0.5
        self.gameover_sound_volume = 0.7

        self.current_song_index = 0
        self.total_song_number = 6

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        # Speed factors
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 1.5
        self.alien_bullet_speed_factor = 0.75
        self.alien_speed_factor = 1

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
