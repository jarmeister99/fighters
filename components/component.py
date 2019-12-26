from components.exceptions import ComponentError


class Component:
    def __init__(self, entity, *required_attributes):
        for attr in required_attributes:
            if not hasattr(entity, attr):
                raise ComponentError(f'Component {entity} cannot be attached to an object without attribute {attr}')
        self.entity = entity
