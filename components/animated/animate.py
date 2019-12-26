import pygame

from components.component import Component


class Animate(Component):
    def __init__(self, entity, animation_elapsed_time=3, animation_time=3):
        super().__init__(entity, 'animation_elapsed_time', 'animation_time', 'animation_steps', 'animations', 'current_animation', 'facing')

    def update(self):
        # Handle animation
        self.entity.animation_elapsed_time += 1
        if self.entity.animation_elapsed_time % self.entity.animation_time == 0:
            self.entity.animation_steps += 1
        animation_index = self.entity.animation_steps % len(self.entity.animations.get(self.entity.current_animation))
        self.entity.image = self.entity.animations.get(self.entity.current_animation)[animation_index]
        if self.entity.facing == 'LEFT':
            self.entity.image = pygame.transform.flip(self.entity.image, True, False)