import pygame

from pygame.math import Vector2
from pygame.locals import *
from events import Events
from Core.Debug import Debug


class Input:
    _movement_axis = Vector2(0, 0)
    events = Events('on_fire')
    ui_events = Events('on_mouse_press')

    @staticmethod
    def get_movement_axis():
        return Input._movement_axis

    @staticmethod
    def get_on_fire_event():
        return Input.events.on_fire

    @staticmethod
    def get_mouse_position():
        x, y = pygame.mouse.get_pos()
        return Vector2(x, y)

    @staticmethod
    def update():
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    Input._movement_axis.x = -1
                elif event.key == pygame.K_RIGHT:
                    Input._movement_axis.x = 1
                elif event.key == pygame.K_UP:
                    Input._movement_axis.y = -1
                elif event.key == pygame.K_DOWN:
                    Input._movement_axis.y = 1
                elif event.key == pygame.K_SPACE:
                    Input.events.on_fire()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                Input.ui_events.on_mouse_press()
            elif event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == KEYUP:
                if event.key == K_LEFT and Input._movement_axis.x == -1:
                    Input._movement_axis.x = 0
                elif event.key == K_RIGHT and Input._movement_axis.x == 1:
                    Input._movement_axis.x = 0
                elif event.key == K_UP and Input._movement_axis.y == -1:
                    Input._movement_axis.y = 0
                elif event.key == K_DOWN and Input._movement_axis.y == 1:
                    Input._movement_axis.y = 0
