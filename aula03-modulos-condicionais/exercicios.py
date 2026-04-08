import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play(start=175.0)  # 🔥 só uma vez aqui

clock = pygame.time.Clock()

while pygame.mixer.music.get_busy():
    clock.tick(30)