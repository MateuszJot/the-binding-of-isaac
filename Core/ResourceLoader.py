import os
import pygame

from Core.Debug import Debug


class ResourceLoader:
    RESOURCES_DIRECTORY_PATH = "Resources/"
    CACHED_SPRITES = {}

    @staticmethod
    def load_sprites_from_folder(local_path):
        directory = f"{os.getcwd()}/../{ResourceLoader.RESOURCES_DIRECTORY_PATH}{local_path}"
        if directory in ResourceLoader.CACHED_SPRITES:
            Debug.log(f"Used cached sprites {len(ResourceLoader.CACHED_SPRITES[directory])} from: {local_path}")
            return ResourceLoader.CACHED_SPRITES[directory]
        sprites = []

        all_png_files = [file for file in os.listdir(directory) if file.lower().endswith(".png")]

        for filename in sorted(all_png_files, key=lambda x: int(x.replace(".png", ""))):
            file_full_name = os.path.join(directory, filename)
            name, extension = os.path.splitext(filename)
            if os.path.isfile(file_full_name) and extension == ".png":
                sprites.append(pygame.image.load(file_full_name))

        Debug.log(f"Loaded {len(sprites)} from: {local_path}")
        ResourceLoader.CACHED_SPRITES[directory] = sprites
        return ResourceLoader.CACHED_SPRITES[directory]

    @staticmethod
    def load_sprite_from_path(local_path):
        directory = f"{os.getcwd()}/../{ResourceLoader.RESOURCES_DIRECTORY_PATH}{local_path}"
        if directory in ResourceLoader.CACHED_SPRITES:
            Debug.log(f"Used cached sprite from: {local_path}")
            return ResourceLoader.CACHED_SPRITES[directory]

        Debug.log(f"Loaded sprite from: {local_path}")
        ResourceLoader.CACHED_SPRITES[directory] = pygame.image.load(directory)
        return ResourceLoader.CACHED_SPRITES[directory]
