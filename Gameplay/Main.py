import pygame
import os
import Core.Settings as Settings
from Core.Input import Input
from Gameplay.GameManager import GameManager


pygame.init()
pygame.display.set_caption("The Binding Of Isaac - Mateusz Jachowicz")
screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
pygame.mixer.music.load(f"{os.getcwd()}/../Resources/Sounds/music.wav")
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.2)
running = True
clock = pygame.time.Clock()

while running:
    GameManager.get_scene().render(screen)
    Input.update()
    GameManager.get_scene().update(clock.tick(Settings.FPS))
    pygame.display.flip()

pygame.quit()
