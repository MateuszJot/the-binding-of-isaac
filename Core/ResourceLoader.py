import os
import pygame

from Core.Debug import Debug


class ResourceLoader:
    RESOURCES_DIRECTORY_PATH = "Resources/"
    @staticmethod
    def load_sprites_from_folder(local_path):
        directory = ResourceLoader.RESOURCES_DIRECTORY_PATH + local_path
        sprites = []

        for filename in os.listdir(os.path.abspath(directory)):
            f = os.path.join(directory, filename)
            name, extension = os.path.splitext(filename)
            if os.path.isfile(f) & extension == ".png":
                sprites.append(pygame.image.load(f))

        Debug.log(f"Loaded {len(sprites)} from: {local_path}")
        return sprites
