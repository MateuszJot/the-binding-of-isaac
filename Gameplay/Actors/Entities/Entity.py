import pygame.mixer
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

    def __init__(self, position, rotation, scale, scene, collision_layer=0, base_health=10):
        self.initialize_movement_animations()
        self._move_direction = Vector2(0, 0)
        self._shadow = None
        self._special_animation = None
        self._collision_layer = collision_layer
        self._health = base_health
        self._damage_sound = ResourceLoader.load_sound_from_path("Sounds/damage.wav")

        super().__init__(position, rotation, scale, None, scene, True, collision_layer)

    def get_center_position(self):
        return self.get_position() + self.get_scale()/2

    def on_update(self, delta_time):
        if self._shadow is None:
            self.create_shadow()

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
            next_frame = self._special_animation.get_next_sprite()
            if next_frame is not None:
                return next_frame
            else:
                self._special_animation = None

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

    def on_collision_enter(self, actor):
        if actor.get_collision_layer() != self._collision_layer:
            return

        self.apply_damage()

    def apply_damage(self, damage=1):
        pygame.mixer.Sound.play(self._damage_sound)
        self._health -= damage
        if self._health <= 0:
            self.create_death_particle()
            self.on_death()
            self._scene.destroy_actor(self._shadow)
            self._scene.destroy_actor(self)
        else:
            self.create_damage_particle()

    def create_shadow(self):
        self._shadow = Actor(Vector2(5, 5), 0, Vector2(2, 2), ResourceLoader.load_sprite_from_path("Misc/shadow.png"), self._scene)
        self._scene.add_actor_at_index(self._shadow, 0)

    def create_death_particle(self):
        pass

    def create_damage_particle(self):
        pass

    def on_death(self):
        pass
