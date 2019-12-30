import pygame

from phys.collision import is_on_ground, copy_faces


class Entity(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()

        self.game = game

        # Physics attributes
        self.move_vector = [0, 0]
        self.move_speed = 0

        # Physical attributes
        self.width = 0
        self.height = 0

        # Image attributes
        self.image = None
        self.rect = None
        self.facing = None

        # Components
        self.components = {}

    def update(self):
        for component in self.components.values():
            component.update()
        self.move()

    def move(self):
        terrain = [tile.rect for tile in self.game.terrain]
        if self.move_vector[0] != 0:
            faces = copy_faces(self.rect)
            face = None
            if self.move_vector[0] < 0:
                face = faces.get('left')
            elif self.move_vector[0] > 0:
                face = faces.get('right')
            to_move = self.move_speed
            while to_move > 0:
                face.left += self.move_vector[0]
                if face.collidelist(terrain) == -1:
                    self.rect.left += (self.move_vector[0] * to_move)
                    to_move = 0
                to_move -= 1

