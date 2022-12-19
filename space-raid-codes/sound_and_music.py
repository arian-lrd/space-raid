import pygame
import random


class Sounds():
    """A class to store sound settings and sound functions."""

    def __init__(self, ai_settings):
        self.ai_settings = ai_settings

    def check_for_new_background_song(self,):
        """If the background music has ended play a ew one."""
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load(self.ai_settings.background_music_files[
                                        self.ai_settings.current_song_index])
            if self.ai_settings.current_song_index == self.ai_settings.total_song_number - 1:
                self.ai_settings.current_song_index = 0
            else:
                self.ai_settings.current_song_index += 1
            pygame.mixer.music.play()

    def play_background_music(self):
        """Play the background music at the beginning of the game.."""
        pygame.mixer.music.set_volume(self.ai_settings.background_music_volume)
        random.shuffle(self.ai_settings.background_music_files)
        pygame.mixer.music.load(
            self.ai_settings.background_music_files[self.ai_settings.current_song_index])
        self.ai_settings.current_song_index += 1
        pygame.mixer.music.play()

    def stop_background_music(self):
        """Stop the background music at the end of the game."""
        pygame.mixer.music.stop()

    def play_menu_music(self):
        """Play the menu music on two occasions.
        1) Before the game starts
        2) After the player loses"""
        pygame.mixer.music.set_volume(self.ai_settings.menu_music_volume)
        pygame.mixer.music.load(self.ai_settings.menu_music_file)
        pygame.mixer.music.play(-1)

    def stop_menu_music(self):
        """Stop the menu music before the game stops."""
        pygame.mixer.music.stop()

    def play_laser_sound(self):
        """Play laser sound when the ship shoots."""
        laser_sound = pygame.mixer.Sound(self.ai_settings.laser_sound_file)
        laser_sound.set_volume(self.ai_settings.laser_sound_volume)
        laser_sound.play()

    def play_alien_explosion_sound(self):
        """Play an explosion sound effect every time an alien ship is hit."""
        explosion_sound = pygame.mixer.Sound(
            self.ai_settings.alien_explosion_sound_file)
        explosion_sound.set_volume(self.ai_settings.explosion_sound_volume)
        explosion_sound.play()

    def play_ship_explosion_sound(self):
        """Play an explosion sound everytime the player's ship is hit."""
        ship_explosion_sound = pygame.mixer.Sound(
            self.ai_settings.ship_explosion_sound_file)
        ship_explosion_sound.set_volume(self.ai_settings.ship_explosion_sound_volume)
        ship_explosion_sound.play()

    def play_alien_reach_bottom_sound(self):
        """Play a sound whenever an alien reaches the bottom of the screen."""
        alien_reach_bottom_sound = pygame.mixer.Sound(
            self.ai_settings.alien_reach_bottom_sound_file)
        alien_reach_bottom_sound.set_volume(
            self.ai_settings.alien_reach_bottom_sound_volume)
        alien_reach_bottom_sound.play()

    def play_gameover_sound(self):
        """Play a sound whenever the player loses."""
        gameover_sound = pygame.mixer.Sound(self.ai_settings.gameover_sound_file)
        gameover_sound.set_volume(self.ai_settings.gameover_sound_volume)
        gameover_sound.play()
