from Core.Actors.Actor import Actor
from pygame.math import Vector2


class UIImage(Actor):
    def __init__(self, position, scale, scene, image):
        super().__init__(Vector2(position.x, position.y), 0, scale, image, scene)
