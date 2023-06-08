from Gameplay.Actors.Entities.Entity import Entity
from Core.Actors.Actor import Actor
from pygame.math import Vector2


class ProjectileActor(Actor):
    def __init__(self, position, rotation, scale,
                 velocity, parent_entity, scene,
                 projectile_animation, collision_layer=0):
        super().__init__(Vector2(position.x, position.y), rotation, scale, None, scene, False, collision_layer)
        self._velocity = Vector2(velocity.x, velocity.y)
        self._parent_entity = parent_entity
        self._projectile_animation = projectile_animation

    def on_update(self, delta_time):
        self.move(self._velocity * delta_time / 100)
        self.look_for_collision()
        self.destroy_if_left_area()

    def get_sprite(self):
        return self._projectile_animation.get_next_sprite()

    @staticmethod
    def is_in_area(position):
        if position.x < Entity.POSITION_MIN_X - 2:
            return False
        elif position.x > Entity.POSITION_MAX_X + 2:
            return False

        if position.y < Entity.POSITION_MIN_Y - 2:
            return False
        elif position.y > Entity.POSITION_MAX_Y + 2:
            return False

        return True

    def destroy_if_left_area(self):
        if not ProjectileActor.is_in_area(self._position):
            self._scene.destroy_actor(self)


