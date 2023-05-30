from Core.Actors.ActorRenderer import ActorRenderer


class Actor:
    def __init__(self, position, rotation, scale, sprite, y_render_order=False, collision_layer = 0):
        self._position = position
        self._rotation = rotation
        self._scale = scale
        self._renderer = ActorRenderer(self)
        self._sprite = sprite
        self._y_render_order = y_render_order
        self.on_start()
        self._collision_layer = collision_layer

    def get_collision_layer(self):
        return self._collision_layer

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

    def get_y_render_order(self):
        return self._y_render_order

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

    def on_collision(self, actor):
        pass

    def look_for_collision(self, scene):
        for actor in scene.get_actors():
            if actor is self:
                continue

            actor_scale = actor.get_scale()
            actor_position = actor.get_position()

            if self._position.x < actor_position.x + actor_scale.x and\
                self._position.x + self._scale.x > actor_position.x and\
                self._position.y < actor_position.y + actor_scale.y and\
                self._position.y + self._scale.y > actor_position.y:
                actor.on_collision(self)

    def move(self, delta):
        self._position += delta
