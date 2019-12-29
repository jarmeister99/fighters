import pygame
import os

from components.animated.gravity import Gravity
from components.animated.animate import Animate
from components.animated.flip_image import FlipImage
from components.animated.running_animation import RunningAnimation
from components.exceptions import ComponentError
from entities.entity import Entity
from utility import spritesheet


class Knight(Entity):
    def __init__(self, x, y, game):
        super().__init__(game)

        # Declare gameplay members
        self.game = game
        self.width = 125
        self.height = 125

        # Declare physics members
        self.move_speed = 9

        # Attach components
        self.components['flip_image'] = FlipImage(self)
        self.components['animate'] = Animate(self)
        self.components['running_animation'] = RunningAnimation(self)
        self.components['gravity'] = Gravity(self)

        # Shortcuts for components
        self.animate = self.components.get('animate')

        # Load components
        self.load_animations()

        # Declare initial state
        self.facing = 'RIGHT'
        self.animate.current_animation = 'idle'
        self.image = self.animate.get_current_animation()[0]

        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y



    def update(self):
        super().update()


    def attack(self):
        pass

    def jump(self):
        pass

    def load_animations(self):
        if not self.components.get('animate'):
            raise ComponentError('Attempted to load animations to an entity without an animate component')
        animation_directory = os.path.abspath('img/entities/knight')

        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'idle.png'))
        self.animate.add_animation('idle', ss.load_strip(64, 64, 15, l_shrink=22, r_shrink=15, t_shrink=12, d_shrink=20))

        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'run.png'))
        self.animate.add_animation('run', ss.load_strip(96, 64, 8, l_shrink=40, r_shrink=32, t_shrink=15, d_shrink=20))

        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'attack.png'))
        self.animate.add_animation('attack', ss.load_strip(96, 64, 8, l_shrink=40, r_shrink=32, t_shrink=15, d_shrink=20))

