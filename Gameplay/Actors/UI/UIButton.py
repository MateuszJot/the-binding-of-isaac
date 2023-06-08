from Core.Actors.Actor import Actor
from Core.Input import Input
from pygame.math import Vector2
from events import Events


class UIButton(Actor):
    def __init__(self, position, scale, scene, image, image_hovered):
        self.events = Events('on_click')
        self._default_image = image
        self._hovered_image = image_hovered
        Input.ui_events.on_mouse_press += self.on_click
        super().__init__(Vector2(position.x, position.y), 0, scale, None, scene)

    def on_click(self):
        if not self.is_hovered():
            return

        self.events.on_click()

    def get_sprite(self):
        if self.is_hovered():
            return self._hovered_image
        else:
            return self._default_image

    def is_hovered(self):
        mouse_position = Input.get_mouse_position()
        my_position = self._renderer.get_position_in_pixels()
        my_scale = self._renderer.get_scale_in_pixels()

        if mouse_position.x < my_position.x:
            return False
        if mouse_position.y < my_position.y:
            return False
        if mouse_position.x > my_position.x + my_scale.x:
            return False
        if mouse_position.y > my_position.y + my_scale.y:
            return False

        return True
