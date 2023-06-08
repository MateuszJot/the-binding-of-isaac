import random
import Gameplay.GameManager

from pygame.math import Vector2
from Gameplay.Actors.Entities.PlayerEntity import PlayerEntity
from Gameplay.Actors.Entities.GhostEntity import GhostEntity
from Gameplay.Actors.Entities.MonsterEntity import MonsterEntity
from Gameplay.Actors.DoorActor import DoorActor
from Core.Scene import Scene


class EndlessScene:
    AVAILABLE_MAPS = ["Scenes/map1.png", "Scenes/map2.png"]

    @staticmethod
    def get_scene(level=0):
        scene = Scene(random.choice(EndlessScene.AVAILABLE_MAPS))
        player = PlayerEntity(Vector2(5, 5), 0, Vector2(2, 2), scene)
        scene.add_actor(player)
        EndlessScene.add_doors_to_scene(scene)

        ghost_amount = EndlessScene.get_ghost_entity_amount_over_level(level)
        monster_amount = EndlessScene.get_monster_entity_amount_over_level(level)
        Gameplay.GameManager.GameManager.set_enemies_alive(ghost_amount + monster_amount)
        for i in range(0, ghost_amount):
            position = Vector2(random.uniform(1, 5), random.uniform(2, 5))
            scene.add_actor(GhostEntity(position, 0, Vector2(2, 2), player, scene))

        for i in range(0, monster_amount):
            position = Vector2(random.uniform(1, 5), random.uniform(2, 5))
            scene.add_actor(MonsterEntity(position, 0, Vector2(2, 2), player, scene))

        return scene

    @staticmethod
    def get_ghost_entity_amount_over_level(level):
        return int(level / 2) + 1

    @staticmethod
    def get_monster_entity_amount_over_level(level):
        base = level - 1
        if base < 0:
            base = 0
        return int(base / 2)

    @staticmethod
    def add_doors_to_scene(scene):
        door_north = DoorActor(Vector2(8.315, 0.6), Vector2(1.4, 0.6), scene)
        door_east = DoorActor(Vector2(17.8, 4.69), Vector2(0.6, 0.7), scene)
        door_south = DoorActor(Vector2(8.48, 9), Vector2(1, 0.6), scene)
        door_west = DoorActor(Vector2(1.4, 4.61), Vector2(0.6, 1), scene)
        scene.add_actor(door_north)
        scene.add_actor(door_east)
        scene.add_actor(door_south)
        scene.add_actor(door_west)
