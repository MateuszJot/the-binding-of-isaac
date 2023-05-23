from pygame.math import *


class SceneCamera:
    _position = Vector2(0, 0)

    @staticmethod
    def get_offset():
        return SceneCamera._position

    @staticmethod
    def set_position(new_position):
        SceneCamera._position = new_position

    @staticmethod
    def move(offset):
        SceneCamera._position += offset


