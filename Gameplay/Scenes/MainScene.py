from pygame.math import Vector2
from Gameplay.Actors.Entities.PlayerEntity import PlayerEntity
from Gameplay.Actors.Entities.GhostEntity import GhostEntity
from Core.Scene import Scene


class MainScene:
    @staticmethod
    def get_scene():
        scene = Scene("Scenes/map2.png")
        player = PlayerEntity(Vector2(5, 5), 0, Vector2(2, 2))
        scene.add_actor(player)
        scene.add_actor(GhostEntity(Vector2(7, 5), 0, Vector2(2, 2), player))
        #scene.add_actor(GhostEntity(Vector2(6, 5), 0, Vector2(2, 2), player))
        #scene.add_actor(GhostEntity(Vector2(4, 5), 0, Vector2(2, 2), player))
        return scene
