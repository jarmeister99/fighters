import pygame

from components.component import Component


class Gravity(Component):
    def __init__(self, entity):
        super().__init__(entity, 'move_vector')

    def update(self):
        if 0 < self.entity.move_vector[1] < 10:
            self.entity.move_vector[1] *= 1.1
