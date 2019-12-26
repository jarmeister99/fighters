from components.component import Component


class FlipImage(Component):
    def __init__(self, entity):
        super().__init__(entity, 'move_vector', 'facing')

    def update(self):
        if self.entity.move_vector[0] == -1:
            self.entity.facing = 'LEFT'
        elif self.entity.move_vector[0] == 1:
            self.entity.facing = 'RIGHT'
