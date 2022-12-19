import pygame

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('music/Arcade - Public Memory.wav')
pygame.mixer.music.load('music/Ambientmain_0.wav')
pygame.mixer.music.load('music/Arcade - Public Memory.wav')

pygame.mixer.music.play(-1)

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(40)