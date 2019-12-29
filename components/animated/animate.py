import pygame

from components.component import Component


class Animate(Component):
    """ Attach to an entity to provide the logic for animation. This component does not determine which animation state
        an entity should be in """

    def __init__(self, entity, animation_time=3):
        super().__init__(entity, 'load_animations')
        self.animation_time = animation_time
        self.animation_elapsed_time = 0
        self.animation_steps = 0
        self.current_animation = None
        self.animations = {}
        self.locked_image = False

    def lock_image(self):
        self.locked_image = True

    def unlock_image(self):
        self.locked_image = False

    def update(self):
        """ Contains the logic for animation """
        if self.locked_image:
            self.entity.image = self.animations.get(self.current_animation)[
                self.animation_steps % len(self.animations.get(self.current_animation))]
        else:
            self.animation_elapsed_time += 1
            if self.animation_elapsed_time % self.animation_time == 0:
                self.animation_steps += 1
            animation_index = self.animation_steps % len(self.animations.get(self.current_animation))
            self.entity.image = self.animations.get(self.current_animation)[animation_index]
        if self.entity.facing == 'LEFT':
            self.entity.image = pygame.transform.flip(self.entity.image, True, False)

    def add_animation(self, anim_key, anim):
        """ Resize an animation to fit the entity and then save """
        self.animations[anim_key] = anim
        self.resize()

    def resize(self):
        """ Resize all animations to fit the entity """
        for key in self.animations.keys():
            for i in range(len(self.animations.get(key))):
                self.animations.get(key)[i] = pygame.transform.scale(self.animations.get(key)[i],
                                                                     (self.entity.width, self.entity.height))

    def get_animations(self):
        """ Returns a list containing keys for all animation states """
        return [key for key in self.animations.keys()]

    def get_current_animation(self):
        """ Return a list containing the images of the current animation sequence """
        return self.animations.get(self.current_animation)
