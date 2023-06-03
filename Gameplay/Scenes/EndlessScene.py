import random

from pygame.math import Vector2
from Gameplay.Actors.Entities.PlayerEntity import PlayerEntity
from Gameplay.Actors.Entities.GhostEntity import GhostEntity
from Core.Scene import Scene
from Gameplay.GameManager import GameManager


class EndlessScene(Scene):
    AVAILABLE_MAPS = ["Scenes/map1.png", "Scenes/map2.png"]

    @staticmethod
    def get_scene(level=0):
        scene = Scene(random.choice(EndlessScene.AVAILABLE_MAPS))
        player = PlayerEntity(Vector2(5, 5), 0, Vector2(2, 2))
        scene.add_actor(player)

        ghost_amount = EndlessScene.get_ghost_entity_amount_over_level(level)
        GameManager.set_enemies_alive(ghost_amount)
        for i in range(0, ghost_amount):
            position = Vector2(random.uniform(1, 5), random.uniform(2, 5))
            scene.add_actor(GhostEntity(position, 0, Vector2(2, 2), player))

        return scene

    @staticmethod
    def get_ghost_entity_amount_over_level(level):
        return int(level / 2) + 1


