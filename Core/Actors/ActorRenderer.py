import pygame
from .. import Settings
from ..SceneCamera import SceneCamera


class ActorRenderer:
    def __init__(self, actor):
        self._actor = actor

    def render(self, window):
        sprite = self._actor.get_sprite()
        if sprite is None:
            return

        sprite = pygame.transform.scale(sprite, self.get_scale_in_pixels())
        sprite = pygame.transform.rotate(sprite, self._actor.get_rotation())

        window.blit(sprite, self.get_position_in_pixels())

    def get_position_in_pixels(self):
        return (self._actor.get_position() - SceneCamera.get_offset()) * Settings.ONE_METER

    def get_scale_in_pixels(self):
        return self._actor.get_scale() * Settings.ONE_METER
