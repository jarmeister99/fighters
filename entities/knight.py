import pygame
import os
from utility import spritesheet


class Knight(pygame.sprite.Sprite):
    def __init__(self, x, y, game):
        super(Knight, self).__init__()

        # Declare gameplay members
        self.game = game
        self.width = 125
        self.height = 125

        # Declare physics members
        self.move_vector = [0, 0]
        self.move_speed = 9

        # Declare animation members
        self.animations = {}
        self.animation_time = 3
        self.animation_elapsed_time = 0
        self.animation_steps = 0
        self.load_animations()
        self.current_animation = 'idle'

        # Declare image variables
        self.image = self.animations.get(self.current_animation)[0]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.facing = 'RIGHT'

    def update(self):
        # Handle logic
        self.move_vector[1] = 10
        self.move()

        # Flip if necessary
        if self.move_vector[0] == -1:
            self.facing = 'LEFT'
            self.current_animation = 'run'
        elif self.move_vector[0] == 1:
            self.facing = 'RIGHT'
            self.current_animation = 'run'
        else:
            self.current_animation = 'idle'

        # Handle animation
        self.animation_elapsed_time += 1
        if self.animation_elapsed_time % self.animation_time == 0:
            self.animation_steps += 1
        animation_index = self.animation_steps % len(self.animations.get(self.current_animation))
        self.image = self.animations.get(self.current_animation)[animation_index]
        if self.facing == 'LEFT':
            self.image = pygame.transform.flip(self.image, True, False)

    def move(self):
        # If we should move along the x axis
        if self.move_vector[0] != 0:
            move_amount = self.move_vector[0] * self.move_speed
            test_rect = pygame.Rect(self.rect.left + move_amount, self.rect.top, 2, self.rect.height)
            if test_rect.collidelist([tile.rect for tile in self.game.tiles]) == -1:
                self.rect.left += move_amount
            else:
                # Get as close to the collider as possible
                closest_movement = 0
                test_rect = pygame.Rect(self.rect.left + closest_movement, self.rect.top, 2, self.rect.height)
                while test_rect.collidelist([tile.rect for tile in self.game.tiles]) == -1:
                    test_rect.left += closest_movement
                    closest_movement += 1
                self.rect.left += closest_movement

        if self.move_vector[1] != 0:
            test_rect = pygame.Rect(self.rect.left, self.rect.top + self.move_vector[1] + self.rect.height,
                                    self.rect.width, 2)
            if test_rect.collidelist([tile.rect for tile in self.game.tiles]) == -1:
                self.rect.top += self.move_vector[1]
            else:
                closest_movement = 0
                test_rect = pygame.Rect(self.rect.left, self.rect.top + closest_movement + self.rect.height,
                                        self.rect.width, 2)
                while test_rect.collidelist([tile.rect for tile in self.game.tiles]) == -1:
                    test_rect.top += closest_movement
                    closest_movement += 1
                self.rect.top += closest_movement

    def load_animations(self):
        animation_directory = os.path.abspath('img/entities/knight')
        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'idle.png'))
        self.animations['idle'] = ss.load_strip(64, 64, 15, l_shrink=22, r_shrink=15, t_shrink=12, d_shrink=20)
        ss = spritesheet.SpriteSheet(os.path.join(animation_directory, 'run.png'))
        self.animations['run'] = ss.load_strip(96, 64, 8, l_shrink=40, r_shrink=32, t_shrink=15, d_shrink=20)
        for key in self.animations.keys():
            for i in range(len(self.animations.get(key))):
                self.animations.get(key)[i] = pygame.transform.scale(self.animations.get(key)[i],
                                                                     (self.width, self.height))
                pygame.image.save(self.animations.get(key)[i], f'{key}{i}.png')
