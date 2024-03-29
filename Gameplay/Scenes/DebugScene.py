from pygame.math import Vector2
from Gameplay.Actors.Entities.PlayerEntity import PlayerEntity
from Gameplay.Actors.Entities.GhostEntity import GhostEntity
from Core.Scene import Scene


class DebugScene:
    @staticmethod
    def get_scene(level=0):
        scene = Scene("Scenes/map2.png")
        player = PlayerEntity(Vector2(5, 5), 0, Vector2(2, 2), scene)
        scene.add_actor(player)
        scene.add_actor(GhostEntity(Vector2(7, 5), 0, Vector2(2, 2), player, scene))
        return scene
