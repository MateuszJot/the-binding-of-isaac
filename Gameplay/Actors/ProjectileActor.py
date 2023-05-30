from Core.SpriteAnimation import SpriteAnimation
from Core.Actors.Actor import Actor
from pygame.math import Vector2


class ProjectileActor(Actor):
    def __init__(self, position, rotation, scale, velocity, parent_entity, scene, projectile_animation):
        super().__init__(Vector2(position.x, position.y), rotation, scale, None)
        self._velocity = Vector2(velocity.x, velocity.y)
        self._parent_entity = parent_entity
        self._scene = scene
        self._projectile_animation = projectile_animation

    def on_update(self, delta_time, scene):
        self.move(self._velocity * delta_time / 100)
        self.look_for_collision(scene)

    def get_sprite(self):
        return self._projectile_animation.get_next_sprite()