import random
import Gameplay.GameManager
from Gameplay.Actors.ParticleActor import ParticleActor
from pygame.math import Vector2
from Core.SpriteAnimation import SpriteAnimation
from Core.ResourceLoader import ResourceLoader
from Gameplay.Actors.Entities.Entity import Entity
from Gameplay.Actors.ProjectileActor import ProjectileActor
from Gameplay.Actors.PhysicsLayers import PhysicsLayers

class GhostEntity(Entity):
    MOVEMENT_SPEED = 0.005
    WALK_ANIMATION_SPEED = 4
    PROJECTILE_ANIMATION_SPEED = 10
    DEATH_EXPLOSION_ANIMATION_SPEED = 2
    DEATH_PARTICLE_TIME = 300
    WALK_SPEED = 0.005
    MIN_DISTANCE_TO_CHANGE_TARGET = 0.1

    DESIRED_POSITION_MIN_X = 1.4
    DESIRED_POSITION_MAX_X = 16.125
    DESIRED_POSITION_MIN_Y = 0.6
    DESIRED_POSITION_MAX_Y = 7.24

    SHOOTING_COOLDOWN_MIN = 500
    SHOOTING_COOLDOWN_MAX = 2000
    LIVES_AMOUNT = 5

    def __init__(self, position, rotation, scale, player):
        super().__init__(position, rotation, scale, PhysicsLayers.MOBS_LAYER, GhostEntity.LIVES_AMOUNT)
        self._player = player
        self._desired_position = None
        self._min_squared_magnitude_to_change_target = GhostEntity.MIN_DISTANCE_TO_CHANGE_TARGET * GhostEntity.MIN_DISTANCE_TO_CHANGE_TARGET
        self._projectile_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Misc/BlueProjectile"), GhostEntity.PROJECTILE_ANIMATION_SPEED)
        self._damage_particle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Misc/Particles/2"), GhostEntity.DEATH_EXPLOSION_ANIMATION_SPEED)
        self._death_particle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Misc/Particles/1"), GhostEntity.DEATH_EXPLOSION_ANIMATION_SPEED)
        self._chose_cooldown = GhostEntity.get_random_cooldown()
        self._current_cooldown = 0
        self.initialize_attack_animations()

    def initialize_attack_animations(self):
        self._attack_left = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/AttackLeft"), GhostEntity.WALK_ANIMATION_SPEED, False)
        self._attack_right = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/AttackRight"), GhostEntity.WALK_ANIMATION_SPEED, False)

    def initialize_movement_animations(self):
        self._idle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/Idle"), GhostEntity.WALK_ANIMATION_SPEED)
        self._walk_left_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/WalkLeft"), GhostEntity.WALK_ANIMATION_SPEED)
        self._walk_right_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Ghost/Animations/WalkRight"), GhostEntity.WALK_ANIMATION_SPEED)
        self._walk_up_animation = self._walk_left_animation
        self._walk_down_animation = self._walk_left_animation

    def on_update(self, delta_time, scene):
        self.update_movement(delta_time)
        self.shoot_projectile_at_player(delta_time)
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

    def shoot_projectile_at_player(self, delta_time):
        if self._current_cooldown < self._chose_cooldown:
            self._current_cooldown += delta_time
            return

        self._current_cooldown = 0
        self._chose_cooldown = GhostEntity.get_random_cooldown()

        to_player_direction = Vector2.normalize(self._player.get_center_position() - self._position)
        projectile_actor = ProjectileActor(self.get_center_position(), 0, Vector2(0.3, 0.3),
                                           to_player_direction, self, self._scene,
                                           self._projectile_animation, PhysicsLayers.PLAYER_LAYER)
        self._scene.add_actor(projectile_actor)
        if to_player_direction.x < 0:
            self._special_animation = self._attack_left
        else:
            self._special_animation = self._attack_right

    def create_death_particle(self, scene):
        scene.add_actor(ParticleActor(self._position - Vector2(0.25, 1), 0, Vector2(3, 3),
                                      scene, self._death_particle_animation, GhostEntity.DEATH_PARTICLE_TIME))

    def create_damage_particle(self, scene):
        scene.add_actor(ParticleActor(self._position - Vector2(0.25, 1), 0, Vector2(3, 3),
                                      scene, self._damage_particle_animation, GhostEntity.DEATH_PARTICLE_TIME))

    def on_death(self):
        Gameplay.GameManager.GameManager.enemy_dead()

    @staticmethod
    def get_random_cooldown():
        return random.uniform(GhostEntity.SHOOTING_COOLDOWN_MIN, GhostEntity.SHOOTING_COOLDOWN_MAX)
