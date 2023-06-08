from Core.Actors.Actor import Actor
from pygame.math import Vector2


class ParticleActor(Actor):
    def __init__(self, position, rotation, scale, scene, animation, live_time):
        super().__init__(Vector2(position.x, position.y), rotation, scale, None, scene)
        self._scene = scene
        self._particle_animation = animation
        self._live_time = live_time
        self._time_alive = 0

    def on_update(self, delta_time):
        self._time_alive += delta_time
        if self._time_alive >= self._live_time:
            self.destroy_particle()

    def destroy_particle(self, ):
        self._scene.destroy_actor(self)

    def get_sprite(self):
        return self._particle_animation.get_next_sprite()
