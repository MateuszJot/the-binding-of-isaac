from pygame.math import Vector2
from Core.Actors.Actor import Actor
from Core.Debug import Debug
from Core.ResourceLoader import ResourceLoader


class Entity(Actor):
    POSITION_MIN_X = 1.4
    POSITION_MAX_X = 16.125
    POSITION_MIN_Y = 0.6
    POSITION_MAX_Y = 7.24
    SHADOW_OFFSET = Vector2(0, 0.8)

    def __init__(self, position, rotation, scale):
        self.initialize_movement_animations()
        self._move_direction = Vector2(0, 0)
        self._shadow = None
        self._special_animation = None

        super().__init__(position, rotation, scale, None, True)

    def on_update(self, delta_time, scene):
        if self._shadow is None:
            self.create_shadow(scene)

        self._shadow.set_position(self._position + Entity.SHADOW_OFFSET)

    def initialize_movement_animations(self):
        self._idle_animation = None
        self._walk_up_animation = None
        self._walk_down_animation = None
        self._walk_left_animation = None
        self._walk_right_animation = None
        Debug.error("Entity basic animations haven't been implemented!")

    def get_sprite(self):
        if self._special_animation is not None:
            return self._special_animation.get_next_sprite()

        if self._move_direction.x == 0 and self._move_direction.y == 0:
            return self._idle_animation.get_next_sprite()

        if self._move_direction.x > 0:
            return self._walk_right_animation.get_next_sprite()
        elif self._move_direction.x < 0:
            return self._walk_left_animation.get_next_sprite()
        elif self._move_direction.y < 0:
            return self._walk_up_animation.get_next_sprite()
        elif self._move_direction.y > 0:
            return self._walk_down_animation.get_next_sprite()

    @staticmethod
    def clamp_position(position):
        if position.x < Entity.POSITION_MIN_X:
            position.x = Entity.POSITION_MIN_X
        elif position.x > Entity.POSITION_MAX_X:
            position.x = Entity.POSITION_MAX_X

        if position.y < Entity.POSITION_MIN_Y:
            position.y = Entity.POSITION_MIN_Y
        elif position.y > Entity.POSITION_MAX_Y:
            position.y = Entity.POSITION_MAX_Y

        return position

    def create_shadow(self, scene):
        self._shadow = Actor(Vector2(5, 5), 0, Vector2(2, 2), ResourceLoader.load_sprite_from_path("Misc/shadow.png"))
        scene.add_actor_at_index(self._shadow, 0)
