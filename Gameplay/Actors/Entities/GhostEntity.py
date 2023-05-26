from pygame.math import Vector2
from Core.SpriteAnimation import SpriteAnimation
from Core.ResourceLoader import ResourceLoader
from Gameplay.Actors.Entities.Entity import Entity


class GhostEntity(Entity):
    ANIMATION_SPEED = 4
    WALK_SPEED = 0.005

    def __init__(self, position, rotation, scale):
        super().__init__(position, rotation, scale)

    def initialize_movement_animations(self):
        self._idle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/Idle"), GhostEntity.ANIMATION_SPEED)
        self._walk_left_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/WalkLeft"), GhostEntity.ANIMATION_SPEED)
        self._walk_right_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/WalkRight"), GhostEntity.ANIMATION_SPEED)
        self._walk_up_animation = self._walk_left_animation
        self._walk_down_animation = self._walk_left_animation

    def on_update(self, delta_time, scene):
        super().on_update(delta_time, scene)
