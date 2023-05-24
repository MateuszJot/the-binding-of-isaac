from pygame.math import Vector2
from Core.Actors.Actor import Actor
from Core.SpriteAnimation import SpriteAnimation
from Core.ResourceLoader import ResourceLoader
from Core.Input import Input
from Core.Debug import Debug


class PlayerActor(Actor):
    ANIMATION_SPEED = 2
    WALK_SPEED = 0.005
    SHADOW_OFFSET = Vector2(0, 0.8)

    POSITION_MIN_X = 1.4
    POSITION_MAX_X = 16.125
    POSITION_MIN_Y = 0.6
    POSITION_MAX_Y = 7.24

    def __init__(self, position, rotation, scale):
        self._idle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/Idle"), PlayerActor.ANIMATION_SPEED)
        self._walk_up_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkUp"), PlayerActor.ANIMATION_SPEED)
        self._walk_down_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkDown"), PlayerActor.ANIMATION_SPEED)
        self._walk_left_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkLeft"), PlayerActor.ANIMATION_SPEED)
        self._walk_right_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkRight"), PlayerActor.ANIMATION_SPEED)
        self._move_direction = Vector2(0, 0)
        self._shadow = None

        super().__init__(position, rotation, scale, None)

    def on_update(self, delta_time, scene):
        self._scene = scene

        if self._shadow is None:
            self.create_shadow()

        self._move_direction = Input.get_movement_axis()
        self.move(self._move_direction * delta_time * PlayerActor.WALK_SPEED)
        self.set_position(self.clamp_position(self._position))
        self._shadow.set_position(self._position + PlayerActor.SHADOW_OFFSET)

    def get_sprite(self):
        if self._move_direction.x > 0:
            return self._walk_right_animation.get_next_sprite()
        elif self._move_direction.x < 0:
            return self._walk_left_animation.get_next_sprite()
        elif self._move_direction.y < 0:
            return self._walk_up_animation.get_next_sprite()
        elif self._move_direction.y > 0:
            return self._walk_down_animation.get_next_sprite()
        else:
            return self._idle_animation.get_next_sprite()

    def create_shadow(self):
        self._shadow = Actor(Vector2(5, 5), 0, Vector2(2, 2), ResourceLoader.load_sprite_from_path("Misc/shadow.png"))
        self._scene.add_actor_at_index(self._shadow, 0)

    @staticmethod
    def clamp_position(position):
        if position.x < PlayerActor.POSITION_MIN_X:
            position.x = PlayerActor.POSITION_MIN_X
        elif position.x > PlayerActor.POSITION_MAX_X:
            position.x = PlayerActor.POSITION_MAX_X

        if position.y < PlayerActor.POSITION_MIN_Y:
            position.y = PlayerActor.POSITION_MIN_Y
        elif position.y > PlayerActor.POSITION_MAX_Y:
            position.y = PlayerActor.POSITION_MAX_Y

        return position
