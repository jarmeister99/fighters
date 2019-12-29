import pygame

from components.component import Component
from phys.collision import is_on_ground


class Gravity(Component):
    def __init__(self, entity, g=0.25, falling_img=None):
        super().__init__(entity)
        self.g = g
        self.falling_img = falling_img
        self.old_img = None

    def update(self):
        if not is_on_ground(self.entity.rect, [terrain.rect for terrain in self.entity.game.terrain]):
            if self.entity.components.get('animate'):
                self.entity.components.get('animate').lock_image()
            if self.entity.move_vector[1] == 0:
                self.entity.move_vector[1] = 1
            else:
                self.entity.move_vector[1] += self.g

        elif self.entity.components.get('animate'):
            self.entity.components.get('animate').unlock_image()
