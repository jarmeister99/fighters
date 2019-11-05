# This class handles sprite sheets
# This was taken from www.scriptefun.com/transcript-2-using
# sprite-sheets-and-drawing-the-background
# I've added some code to fail if the file wasn't found..
# Note: When calling images_at the rect is the format:
# (x, y, x + offset, y + offset)

import pygame


class SpriteSheet(object):
    def __init__(self, filename):
        try:
            self.sheet = pygame.image.load(filename).convert_alpha()
        except pygame.error as e:
            print(f'Unable to load spritesheet image: {filename}')
            raise SystemExit(e)

    def load_strip(self, width, height, count, l_shrink=0, r_shrink=0, t_shrink=0, d_shrink=0):
        images = []
        for i in range(count):
            rect = pygame.Rect((width * i) + l_shrink, t_shrink, width - (l_shrink + r_shrink), height - (t_shrink + d_shrink))
            image = pygame.Surface(rect.size, pygame.SRCALPHA).convert_alpha()
            image.blit(self.sheet, (0, 0), rect)
            images.append(image)
        return images
