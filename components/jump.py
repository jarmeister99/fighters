import pygame

from components.component import Component
from phys.collision import is_on_ground


class Jump(Component):
    def __init__(self, entity, jump_strength):
        super().__init__(entity)
        self.jump_strength = jump_strength

    def update(self):
        pass


    def jump(self):
        if is_on_ground(self.entity.rect, [terrain.rect for terrain in self.entity.game.terrain]):
            self.entity.move_vector[1] = -self.jump_strength

    def op_jump(self):
        self.entity.move_vector[1] = -self.jump_strength

