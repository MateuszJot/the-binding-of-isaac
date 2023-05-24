from Core.Actors.ActorRenderer import ActorRenderer


class Actor:
    def __init__(self, position, rotation, scale, sprite):
        self._position = position
        self._rotation = rotation
        self._scale = scale
        self._renderer = ActorRenderer(self)
        self._sprite = sprite
        self.on_start()


    def get_position(self):
        return self._position

    def set_position(self, position):
        self._position = position

    def get_rotation(self):
        return self._rotation

    def get_scale(self):
        return self._scale

    def get_renderer(self):
        return self._renderer

    def get_sprite(self):
        return self._sprite

    def render(self, window):
        self._renderer.render(window)

    def on_start(self):
        pass

    def on_update(self, delta_time, scene):
        pass

    def on_destroy(self):
        pass

    def move(self, delta):
        self._position += delta
