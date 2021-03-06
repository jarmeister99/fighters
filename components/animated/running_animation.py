import pygame

from components.component import Component


class RunningAnimation(Component):
    def __init__(self, entity):
        super().__init__(entity, 'animate')

    def update(self):
        if self.entity.move_vector[0] != 0:
            self.entity.components.get('animate').current_animation = 'run'
        else:
            self.entity.components.get('animate').current_animation = 'idle'
