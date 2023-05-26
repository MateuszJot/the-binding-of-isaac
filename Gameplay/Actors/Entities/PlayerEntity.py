from pygame.math import Vector2
from Core.SpriteAnimation import SpriteAnimation
from Core.ResourceLoader import ResourceLoader
from Core.Input import Input
from Gameplay.Actors.Entities.Entity import Entity


class PlayerEntity(Entity):
    ANIMATION_SPEED = 2
    WALK_SPEED = 0.005

    def __init__(self, position, rotation, scale):
        super().__init__(position, rotation, scale)

    def initialize_movement_animations(self):
        self._idle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/Idle"), PlayerEntity.ANIMATION_SPEED)
        self._walk_up_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkUp"), PlayerEntity.ANIMATION_SPEED)
        self._walk_down_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkDown"), PlayerEntity.ANIMATION_SPEED)
        self._walk_left_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkLeft"), PlayerEntity.ANIMATION_SPEED)
        self._walk_right_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkRight"), PlayerEntity.ANIMATION_SPEED)

    def on_update(self, delta_time, scene):
        self._move_direction = Input.get_movement_axis()
        self.move(self._move_direction * delta_time * PlayerEntity.WALK_SPEED)
        self.set_position(self.clamp_position(self._position))
        super().on_update(delta_time, scene)
