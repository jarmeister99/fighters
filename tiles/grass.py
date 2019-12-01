import pygame
import os


class Grass(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super(Grass, self).__init__()
        self.width = width
        self.height = height
        self.image = None
        self.image = self.load_image()
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def load_image(self):
        image_directory = os.path.abspath('img/tiles')
        image_path = os.path.join(image_directory, 'grass.png')
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except pygame.error as e:
            print(f'Unable to load image {image_path}')
            raise SystemExit(e)
        return pygame.transform.scale(self.image, (self.width, self.height))
