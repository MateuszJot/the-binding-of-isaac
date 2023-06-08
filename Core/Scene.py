import pygame
import pygame.math
import Core.Settings as Settings
from Core.ResourceLoader import ResourceLoader


class Scene:
    def __init__(self, background_image_path, level=0):
        self._actors = []
        self._time = 0
        self._background = pygame.transform.scale(ResourceLoader.load_sprite_from_path(background_image_path), (Settings.SCREEN_WIDTH, Settings.SCREEN_HEIGHT))

    def destroy_actor(self, actor):
        if actor not in self._actors:
            return
        self._actors.remove(actor)
        del actor

    def get_actors(self):
        return self._actors

    def add_actor(self, actor):
        if actor not in self._actors:
            self._actors.append(actor)

    def add_actor_at_index(self, actor, index):
        if actor not in self._actors:
            self._actors.insert(index, actor)

    def render(self, window):
        window.blit(self._background, (0, 0))
        actors_with_y_render_order = [x for x in self._actors if x.get_y_render_order()]
        actors_with_y_render_order = sorted(actors_with_y_render_order, key=lambda x: x.get_position().y)
        actors_with_y_render_order_index = 0

        for actor in self._actors:
            if actor.get_y_render_order():
                actors_with_y_render_order[actors_with_y_render_order_index].render(window)
                actors_with_y_render_order_index += 1
            else:
                actor.render(window)

    def update(self, delta_time):
        for actor in self._actors:
            actor.on_update(delta_time, self)
