import pygame

from components.component import Component
from phys.collision import is_on_ground


class Jump(Component):
    def __init__(self, entity, jump_strength=10):
        super().__init__(entity, 'gravity')
        self.jump_strength = jump_strength

    def update(self):
        pass


    def jump(self):
        if is_on_ground(self.entity.rect, [terrain.rect for terrain in self.entity.game.terrain]):
            self.entity.components.get('gravity').y_push = -self.jump_strength

    def op_jump(self):
        self.entity.components.get('gravity').y_push = -self.jump_strength

