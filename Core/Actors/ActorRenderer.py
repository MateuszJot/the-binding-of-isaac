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

        position_in_pixels = (self._actor.get_position() - SceneCamera.get_offset()) * Settings.ONE_METER
        scale_in_pixels = self._actor.get_scale() * Settings.ONE_METER

        sprite = pygame.transform.scale(sprite, scale_in_pixels)
        sprite = pygame.transform.rotate(sprite, self._actor.get_rotation())

        window.blit(sprite, position_in_pixels)
