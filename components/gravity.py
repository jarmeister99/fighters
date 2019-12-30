import pygame

from components.component import Component
from phys.collision import is_on_ground


class Gravity(Component):
    def __init__(self, entity, g=0.25, max_pull=10, falling_img=None):
        super().__init__(entity)
        self.g = g
        self.max_pull = max_pull
        self.falling_img = falling_img
        self.old_img = None
        self.y_push = 0

    def update(self):

        # If the entity is in air
        if not is_on_ground(self.entity.rect, [terrain.rect for terrain in self.entity.game.terrain]):
            # Lock the animation while the entity is in air
            if self.entity.components.get('animate'):
                self.entity.components.get('animate').lock_image()

            # If the entity is not at max velocity
            if self.y_push <= self.max_pull:
                # Increase its velocity by g
                self.y_push += self.g

        # If the entity is on the ground
        else:
            if self.entity.components.get('animate'):
                self.entity.components.get('animate').unlock_image()

        if self.y_push > 0:
            self.entity.move_vector[1] = 1
        elif self.y_push < 0:
            self.entity.move_vector[1] = -1
        else:
            self.entity.move_vector[1] = 0
