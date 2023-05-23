import pygame
from pygame.math import Vector2
from pygame.locals import *
from events import Events


class Input:
    _movement_axis = Vector2(0, 0)
    _events = Events('on_fire')

    @staticmethod
    def get_movement_axis():
        return Input._movement_axis

    @staticmethod
    def get_on_fire_event():
        return Input._events.on_fire

    @staticmethod
    def update():
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    Input._movement_axis.x = -1
                elif event.key == K_RIGHT:
                    Input._movement_axis.x = 1
                elif event.key == K_UP:
                    Input._movement_axis.y = 1
                elif event.key == K_DOWN:
                    Input._movement_axis.y = -1
                elif event.key == K_SPACE:
                    Input._events.on_fire()
            elif event.type == KEYUP:
                if event.key == K_LEFT & Input._movement_axis.x == -1:
                    Input._movement_axis.x = 0
                elif event.key == K_RIGHT & Input._movement_axis.x == 1:
                    Input._movement_axis.x = 0
                elif event.key == K_UP & Input._movement_axis.y == 1:
                    Input._movement_axis.y = 0
                elif event.key == K_DOWN & Input._movement_axis.y == -1:
                    Input._movement_axis.y = 0
