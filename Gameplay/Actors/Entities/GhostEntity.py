import random
import pygame.math
from pygame.math import Vector2
from Core.SpriteAnimation import SpriteAnimation
from Core.ResourceLoader import ResourceLoader
from Gameplay.Actors.Entities.Entity import Entity


class GhostEntity(Entity):
    MOVEMENT_SPEED = 0.005
    ANIMATION_SPEED = 4
    WALK_SPEED = 0.005
    MIN_DISTANCE_TO_CHANGE_TARGET = 0.1

    DESIRED_POSITION_MIN_X = 1.4
    DESIRED_POSITION_MAX_X = 16.125
    DESIRED_POSITION_MIN_Y = 0.6
    DESIRED_POSITION_MAX_Y = 7.24

    def __init__(self, position, rotation, scale, player):
        self._player = player
        self._desired_position = None
        self._min_squared_magnitude_to_change_target = GhostEntity.MIN_DISTANCE_TO_CHANGE_TARGET * GhostEntity.MIN_DISTANCE_TO_CHANGE_TARGET
        super().__init__(position, rotation, scale)

    def initialize_movement_animations(self):
        self._idle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/Idle"), GhostEntity.ANIMATION_SPEED)
        self._walk_left_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/WalkLeft"), GhostEntity.ANIMATION_SPEED)
        self._walk_right_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/WalkRight"), GhostEntity.ANIMATION_SPEED)
        self._walk_up_animation = self._walk_left_animation
        self._walk_down_animation = self._walk_left_animation

    def on_update(self, delta_time, scene):
        self.update_movement(delta_time)
        super().on_update(delta_time, scene)

    def update_movement(self, delta_time):
        direction = self.get_desired_movement_direction()
        frame_movement = direction * delta_time * GhostEntity.MOVEMENT_SPEED

        self._move_direction = direction
        self.move(frame_movement)

    def get_desired_movement_direction(self):
        if self._desired_position is None:
            self._desired_position = Vector2(random.uniform(GhostEntity.DESIRED_POSITION_MIN_X, GhostEntity.DESIRED_POSITION_MAX_X),
                                             random.uniform(GhostEntity.DESIRED_POSITION_MIN_Y, GhostEntity.DESIRED_POSITION_MAX_Y))

        direction = self._desired_position - self._position
        normalized_direction = Vector2.normalize(direction)

        if Vector2.magnitude_squared(direction) <= self._min_squared_magnitude_to_change_target:
            self._desired_position = None

        return normalized_direction
