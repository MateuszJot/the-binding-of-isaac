import pygame
import Core.Settings as Settings

from Core.Input import Input
from Gameplay.Scenes.MainScene import MainScene


pygame.init()
screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
scene = MainScene.get_scene()
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scene.render(screen)
    Input.update()
    scene.update(clock.tick(Settings.FPS))
    pygame.display.flip()

pygame.quit()
