from pygame.math import Vector2
from Gameplay.Actors.Entities.PlayerEntity import PlayerEntity
from Gameplay.Actors.Entities.GhostEntity import GhostEntity
from Core.Scene import Scene


class MainScene:
    @staticmethod
    def get_scene():
        scene = Scene("Scenes/map2.png")
        scene.add_actor(PlayerEntity(Vector2(5, 5), 0, Vector2(2, 2)))
        scene.add_actor(GhostEntity(Vector2(7, 5), 0, Vector2(2, 2)))
        return scene
