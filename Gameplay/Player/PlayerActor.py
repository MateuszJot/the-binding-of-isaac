from pygame.math import Vector2
from Core.Actors.Actor import Actor
from Core.SpriteAnimation import SpriteAnimation
from Core.ResourceLoader import ResourceLoader
from Core.Input import Input


class PlayerActor(Actor):
    ANIMATION_SPEED = 2
    WALK_SPEED = 0.005

    def __init__(self, position, rotation, scale):
        self._idle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/Idle"), PlayerActor.ANIMATION_SPEED)
        self._walk_up_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkUp"), PlayerActor.ANIMATION_SPEED)
        self._walk_down_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkDown"), PlayerActor.ANIMATION_SPEED)
        self._walk_left_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkLeft"), PlayerActor.ANIMATION_SPEED)
        self._walk_right_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkRight"), PlayerActor.ANIMATION_SPEED)
        self._move_direction = Vector2(0 ,0)

        super().__init__(position, rotation, scale, None)

    def on_update(self, delta_time):
        self._move_direction = Input.get_movement_axis()
        self.move(self._move_direction * delta_time * PlayerActor.WALK_SPEED)


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