import pygame
import Settings
from Scene import Scene
from Core.Actors.Actor import Actor
from pygame.math import Vector2


pygame.init()
screen = pygame.display.set_mode((Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))
scene = Scene()

tree_sprite = pygame.image.load("../Resources/tree.png")
tree = Actor(Vector2(2, 2), 0, Vector2(1, 1), tree_sprite)
scene.add_actor(tree)

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    scene.render(screen)
    scene.update(clock.tick(Settings.FPS))
    pygame.display.flip()

pygame.quit()
