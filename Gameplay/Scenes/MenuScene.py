from Gameplay.Actors.UI.UIImage import UIImage
from Gameplay.Actors.UI.UIButton import UIButton
from Core.ResourceLoader import ResourceLoader
from Core.Scene import Scene
from pygame.math import Vector2

import Gameplay.GameManager
import pygame



class MenuScene:
    @staticmethod
    def get_scene(level=0):
        scene = Scene("Scenes/map2.png")
        scene.add_actor(UIImage(Vector2(3, 3), Vector2(4, 2), scene, ResourceLoader.load_sprite_from_path("UI/logo.png")))

        play_button = UIButton(Vector2(3, 5), Vector2(4, 0.75), scene, ResourceLoader.load_sprite_from_path("UI/Buttons/play_default.png"),
                                                                       ResourceLoader.load_sprite_from_path("UI/Buttons/play_hovered.png"))
        credits_button = UIButton(Vector2(3, 6), Vector2(4, 0.75), scene, ResourceLoader.load_sprite_from_path("UI/Buttons/credits_default.png"),
                                                                          ResourceLoader.load_sprite_from_path("UI/Buttons/credits_hovered.png"))
        exit_button = UIButton(Vector2(3, 7), Vector2(4, 0.75), scene, ResourceLoader.load_sprite_from_path("UI/Buttons/exit_default.png"),
                                                                       ResourceLoader.load_sprite_from_path("UI/Buttons/exit_hovered.png"))

        play_button.events.on_click += MenuScene.start_game
        credits_button.events.on_click += MenuScene.to_credits
        exit_button.events.on_click += MenuScene.exit

        scene.add_actor(play_button)
        scene.add_actor(credits_button)
        scene.add_actor(exit_button)
        return scene

    @staticmethod
    def start_game():
        Gameplay.GameManager.GameManager.start_game()

    @staticmethod
    def to_credits():
        Gameplay.GameManager.GameManager.to_credits()

    @staticmethod
    def exit():
        pygame.quit()
