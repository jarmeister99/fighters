import pygame

from components.component import Component


class RunningAnimation(Component):
    def __init__(self, entity):
        super().__init__(entity, 'move_vector', 'current_animation')

    def update(self):
        if self.entity.move_vector[0] != 0:
            self.entity.current_animation = 'run'
        else:
            self.entity.current_animation = 'idle'
