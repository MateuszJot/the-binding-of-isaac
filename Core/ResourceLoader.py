import os
import pygame

from Core.Debug import Debug


class ResourceLoader:
    RESOURCES_DIRECTORY_PATH = "Resources/"
    @staticmethod
    def load_sprites_from_folder(local_path):
        directory = f"{os.getcwd()}/../{ResourceLoader.RESOURCES_DIRECTORY_PATH}{local_path}"
        sprites = []

        for filename in os.listdir(directory):
            file_full_name = os.path.join(directory, filename)
            name, extension = os.path.splitext(filename)
            if os.path.isfile(file_full_name) and extension == ".png":
                sprites.append(pygame.image.load(file_full_name))

        Debug.log(f"Loaded {len(sprites)} from: {local_path}")
        return sprites

    @staticmethod
    def load_sprite_from_path(local_path):
        directory = f"{os.getcwd()}/../{ResourceLoader.RESOURCES_DIRECTORY_PATH}{local_path}"
        Debug.log(f"Loaded sprite from: {local_path}")
        return pygame.image.load(directory)