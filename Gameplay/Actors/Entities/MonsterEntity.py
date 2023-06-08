import random
import Gameplay.GameManager
from Gameplay.Actors.ParticleActor import ParticleActor
from pygame.math import Vector2
from Core.SpriteAnimation import SpriteAnimation
from Core.ResourceLoader import ResourceLoader
from Gameplay.Actors.Entities.Entity import Entity
from Gameplay.Actors.PhysicsLayers import PhysicsLayers


class MonsterEntity(Entity):
    MOVEMENT_SPEED = 0.001
    WALK_ANIMATION_SPEED = 4
    DEATH_EXPLOSION_ANIMATION_SPEED = 2
    DEATH_PARTICLE_TIME = 300

    DESIRED_DISTANCE_TO_PLAYER = 0.7
    DISTANCE_TO_ATTACK_PLAYER = 1
    ATTACK_DAMAGE = 1

    ATTACK_COOLDOWN = 3000

    LIVES_AMOUNT = 2

    def __init__(self, position, rotation, scale, player):
        super().__init__(position, rotation, scale, PhysicsLayers.MOBS_LAYER, MonsterEntity.LIVES_AMOUNT)
        self._player = player
        self._damage_particle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Misc/Particles/2"), MonsterEntity.DEATH_EXPLOSION_ANIMATION_SPEED)
        self._death_particle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Misc/Particles/1"), MonsterEntity.DEATH_EXPLOSION_ANIMATION_SPEED)
        self._current_cooldown = 0
        self.initialize_attack_animations()

    def initialize_attack_animations(self):
        self._attack_left = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Monster/Animations/AttackLeft"), MonsterEntity.WALK_ANIMATION_SPEED, False)
        self._attack_right = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Monster/Animations/AttackRight"), MonsterEntity.WALK_ANIMATION_SPEED, False)

    def initialize_movement_animations(self):
        self._idle_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Monster/Animations/Idle"), MonsterEntity.WALK_ANIMATION_SPEED)
        self._walk_left_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Monster/Animations/WalkLeft"), MonsterEntity.WALK_ANIMATION_SPEED)
        self._walk_right_animation = SpriteAnimation(ResourceLoader.load_sprites_from_folder("Monster/Animations/WalkRight"), MonsterEntity.WALK_ANIMATION_SPEED)
        self._walk_up_animation = self._walk_left_animation
        self._walk_down_animation = self._walk_left_animation

    def on_update(self, delta_time, scene):
        self.update_movement(delta_time)
        self.update_cooldown(delta_time)
        self.try_attack_player()
        super().on_update(delta_time, scene)

    def update_cooldown(self, delta_time):
        if self._current_cooldown > 0:
            self._current_cooldown -= delta_time

    def update_movement(self, delta_time):
        if self._position.distance_to(self._player.get_position()) <= MonsterEntity.DESIRED_DISTANCE_TO_PLAYER:
            return

        direction = Vector2.normalize(self._player.get_position() - self._position)
        frame_movement = direction * delta_time * MonsterEntity.MOVEMENT_SPEED

        self._move_direction = direction
        self.move(frame_movement)

    def try_attack_player(self):
        if self._current_cooldown > 0:
            return

        self._current_cooldown = MonsterEntity.ATTACK_COOLDOWN

        if self._position.distance_to(self._player.get_position()) > MonsterEntity.DISTANCE_TO_ATTACK_PLAYER:
            return

        if self._player.get_position().x < self._position.x:
            self._special_animation = self._attack_left
        else:
            self._special_animation = self._attack_right
        self._player.apply_damage(MonsterEntity.ATTACK_DAMAGE)

    def create_death_particle(self, scene):
        scene.add_actor(ParticleActor(self._position - Vector2(0.25, 1), 0, Vector2(3, 3),
                                      scene, self._death_particle_animation, MonsterEntity.DEATH_PARTICLE_TIME))

    def create_damage_particle(self, scene):
        scene.add_actor(ParticleActor(self._position - Vector2(0.25, 1), 0, Vector2(3, 3),
                                      scene, self._damage_particle_animation, MonsterEntity.DEATH_PARTICLE_TIME))

    def on_death(self):
        Gameplay.GameManager.GameManager.enemy_dead()
