import pygame
import os

class SolidTile(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, img_file):
        super(SolidTile, self).__init__()
        self.width = width
        self.height = height
        self.image = None
        self.image = self.load_image(img_file)
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def load_image(self, img_file):
        image_directory = os.path.abspath('img/tiles')
        image_path = os.path.join(image_directory, img_file)
        try:
            self.image = pygame.image.load(image_path).convert_alpha()
        except pygame.error as e:
            print(f'Unable to load image {image_path}')
            raise SystemExit(e)
        return pygame.transform.scale(self.image, (self.width, self.height))


