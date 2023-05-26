import pygame
import Core.Settings as Settings
from Core.Input import Input
from Gameplay.Scenes.MainScene import MainScene


pygame.init()
pygame.display.set_caption("The Binding Of Isaac - Mateusz Jachowicz")
screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
scene = MainScene.get_scene()
running = True
clock = pygame.time.Clock()

while running:
    scene.render(screen)
    Input.update()
    scene.update(clock.tick(Settings.FPS))
    pygame.display.flip()

pygame.quit()
