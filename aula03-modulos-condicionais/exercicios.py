#faça um programa em python que abra e reproduza o audio de um arquivo MP3

import pygame

# Inicializa o mixer do pygame
pygame.init()

# Carrega o arquivo mp3
pygame.mixer.music.load('musica.mp3')

# Toca o arquivo
pygame.mixer.music.play()
input()
pygame.event.wait()
