# - DESAFIO 021: FAÇA UM PROGRAMA EM PYTHON QUE ABRA E REPRODUZA UM ARQUIVO MP3! -
import pygame
pygame.init()
pygame.mixer_music.load('ex021.mp3')
pygame.mixer_music.play()
input()