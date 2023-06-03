import Gameplay.GameManager

from Core.Actors.Actor import Actor
from pygame.math import Vector2
from Gameplay.Actors.PhysicsLayers import PhysicsLayers


class DoorActor(Actor):
    def __init__(self, position, scale):
        self._doors_enabled = False
        super().__init__(Vector2(position.x, position.y), 0, scale, None, False, PhysicsLayers.PLAYER_LAYER)
        Gameplay.GameManager.GameManager.events.on_all_enemies_dead += self.enable_doors

    def on_update(self, delta_time, scene):
        if self._doors_enabled:
            self.look_for_collision(scene)

    def get_sprite(self):
        return None

    def enable_doors(self):
        self._doors_enabled = True




