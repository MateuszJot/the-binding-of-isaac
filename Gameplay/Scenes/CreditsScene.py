from Gameplay.Actors.UI.UIImage import UIImage
from Gameplay.Actors.UI.UIButton import UIButton
from Core.ResourceLoader import ResourceLoader
from Core.Scene import Scene
from pygame.math import Vector2

import Gameplay.GameManager


class CreditsScene:
    @staticmethod
    def get_scene(level=0):
        scene = Scene("Scenes/map2.png")
        credits = UIImage(Vector2(6.5, 2), Vector2(7, 5), scene, ResourceLoader.load_sprite_from_path("UI/credits.png"))
        to_menu = UIButton(Vector2(8, 7.5), Vector2(4, 0.75), scene, ResourceLoader.load_sprite_from_path("UI/Buttons/to_menu_default.png"),
                                                                     ResourceLoader.load_sprite_from_path("UI/Buttons/to_menu_hovered.png"))

        to_menu.events.on_click += CreditsScene.to_menu

        scene.add_actor(to_menu)
        scene.add_actor(credits)
        return scene

    @staticmethod
    def to_menu():
        Gameplay.GameManager.GameManager.to_main_menu()
