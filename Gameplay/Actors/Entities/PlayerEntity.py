import Gameplay.GameManager

from pygame.math import Vector2
from Core.SpriteAnimation import SpriteAnimation
from Core.ResourceLoader import ResourceLoader
from Core.Input import Input
from Gameplay.Actors.Entities.Entity import Entity
from Gameplay.Actors.ProjectileActor import ProjectileActor
from Gameplay.Actors.PhysicsLayers import PhysicsLayers
from Gameplay.Actors.ParticleActor import ParticleActor
from Gameplay.Actors.DoorActor import DoorActor

import Gameplay.GameManager


class PlayerEntity(Entity):
    WALK_ANIMATION_SPEED = 2
    PROJECTILE_ANIMATION_SPEED = 10
    WALK_SPEED = 0.005
    SHOOTING_COOLDOWN = 2
    DEATH_EXPLOSION_ANIMATION_SPEED = 2
    DEATH_PARTICLE_TIME = 300

    def __init__(self, position, rotation, scale, scene):
        super().__init__(position, rotation, scale, scene, PhysicsLayers.PLAYER_LAYER)
        Input.events.on_fire += self.fire_projectile
        self._cached_move_direction = Vector2(1, 0)
        self._projectile_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Misc/YellowProjectile"), PlayerEntity.PROJECTILE_ANIMATION_SPEED)
        self._damage_particle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Misc/Particles/3"), PlayerEntity.DEATH_EXPLOSION_ANIMATION_SPEED)
        self._death_particle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Misc/Particles/1"), PlayerEntity.DEATH_EXPLOSION_ANIMATION_SPEED)
        self._shooting_cooldown_time = PlayerEntity.SHOOTING_COOLDOWN

    def initialize_movement_animations(self):
        self._idle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/Idle"), PlayerEntity.WALK_ANIMATION_SPEED)
        self._walk_up_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkUp"), PlayerEntity.WALK_ANIMATION_SPEED)
        self._walk_down_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkDown"), PlayerEntity.WALK_ANIMATION_SPEED)
        self._walk_left_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkLeft"), PlayerEntity.WALK_ANIMATION_SPEED)
        self._walk_right_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Player/Animations/WalkRight"), PlayerEntity.WALK_ANIMATION_SPEED)

    def on_update(self, delta_time):
        self.update_movement(delta_time)
        self.fire_cooldown(delta_time)
        super().on_update(delta_time)

    def fire_cooldown(self, delta_time):
        if self._shooting_cooldown_time < PlayerEntity.SHOOTING_COOLDOWN:
            self._shooting_cooldown_time += delta_time / 300

    def update_movement(self, delta_time):
        self._move_direction = Input.get_movement_axis()
        self.move(self._move_direction * delta_time * PlayerEntity.WALK_SPEED)
        self.set_position(self.clamp_position(self._position))

        if self._move_direction.x != 0 or self._move_direction.y != 0:
            self._cached_move_direction = Vector2(self._move_direction.x, self._move_direction.y)

    def create_death_particle(self):
        self._scene.add_actor(ParticleActor(self._position - Vector2(0.25, 1), 0, Vector2(3, 3), self._scene,
                                            self._death_particle_animation, PlayerEntity.DEATH_PARTICLE_TIME))

    def create_damage_particle(self):
        self._scene.add_actor(ParticleActor(self._position - Vector2(0.25, 1), 0, Vector2(3, 3), self._scene,
                                            self._damage_particle_animation, PlayerEntity.DEATH_PARTICLE_TIME))

    def fire_projectile(self):
        if self._shooting_cooldown_time < PlayerEntity.SHOOTING_COOLDOWN:
            return

        self._shooting_cooldown_time = 0
        self._scene.add_actor(ProjectileActor(self.get_center_position(), 0, Vector2(0.3, 0.3), self._cached_move_direction, self, self._scene, self._projectile_animation))

    def on_collision_enter(self, actor):
        if type(actor) is DoorActor:
            Gameplay.GameManager.GameManager.to_next_level()
        else:
            super().on_collision_enter(actor)

    def on_death(self):
        Gameplay.GameManager.GameManager.to_main_menu()
