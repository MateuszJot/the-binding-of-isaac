import Gameplay.Scenes.EndlessScene
from events import Events


class GameManager:
    _level = 0
    _scene = None
    _enemies_alive = 0
    events = Events('on_all_enemies_dead')

    @staticmethod
    def enemy_dead():
        GameManager._enemies_alive -= 1
        if GameManager._enemies_alive == 0:
            GameManager.events.on_all_enemies_dead()

    @staticmethod
    def set_enemies_alive(amount):
        GameManager._enemies_alive = amount

    @staticmethod
    def get_scene():
        if GameManager._scene is None:
            GameManager._scene = Gameplay.Scenes.EndlessScene.EndlessScene.get_scene(GameManager._level)

        return GameManager._scene

    @staticmethod
    def to_next_level():
        GameManager._level += 1
        GameManager._scene = Gameplay.Scenes.EndlessScene.EndlessScene.get_scene(GameManager._level)
