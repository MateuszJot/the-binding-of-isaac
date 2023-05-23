import pygame


class SpriteAnimation:
    def __init__(self, sprites):
        self._sprite_index = 0
        self._sprites = sprites

    def get_next_sprite(self):
        sprite = self._sprites[self._sprite_index]

        self._sprite_index += 1
        if self._sprite_index >= len(self._sprites):
            self._sprite_index = 0

        return sprite

    def __getitem__(self, item):
        return self._sprites[item]
