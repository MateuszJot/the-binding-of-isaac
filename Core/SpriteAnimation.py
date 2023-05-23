import pygame
import math

class SpriteAnimation:
    def __init__(self, sprites, frame_time):
        self._sprite_index = 0
        self._frame_time = frame_time
        self._sprites = sprites

    def get_next_sprite(self):
        sprite = self._sprites[math.floor(self._sprite_index / self._frame_time)]

        self._sprite_index += 1
        if self._sprite_index >= len(self._sprites) * self._frame_time:
            self._sprite_index = 0

        return sprite

    def __getitem__(self, item):
        return self._sprites[item]
