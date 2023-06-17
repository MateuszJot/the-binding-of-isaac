from Core.Actors.ActorRenderer import ActorRenderer


class Actor:
    def __init__(self, position, rotation, scale, sprite, scene, y_render_order=False, collision_layer=0):
        self._position = position
        self._rotation = rotation
        self._scale = scale
        self._renderer = ActorRenderer(self)
        self._sprite = sprite
        self._y_render_order = y_render_order
        self._collision_layer = collision_layer
        self._collided_actors = []
        self._scene = scene
        self.on_start()

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

    def on_update(self, delta_time):
        pass

    def on_destroy(self):
        pass

    def on_collision_enter(self, actor):
        pass

    def on_collision_exit(self, actor):
        pass

    def look_for_collision(self):
        _current_collisions = []
        for actor in self._scene.get_actors():
            if actor is self:
                continue

            actor_scale = actor.get_scale()
            actor_position = actor.get_position()

            if self._position.x < actor_position.x + actor_scale.x and\
                self._position.x + self._scale.x > actor_position.x and\
                self._position.y < actor_position.y + actor_scale.y and\
                self._position.y + self._scale.y > actor_position.y:
                _current_collisions.append(actor)

        for collided_actor in self._collided_actors:
            if collided_actor not in _current_collisions:
                collided_actor.on_collision_exit(self)

        for collided_actor in _current_collisions:
            if collided_actor not in self._collided_actors:
                collided_actor.on_collision_enter(self)

        self._collided_actors = _current_collisions

    def move(self, delta):
        self._position += delta
