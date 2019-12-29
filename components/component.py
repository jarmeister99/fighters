from components.exceptions import ComponentError
from entities.entity import Entity


class Component:
    def __init__(self, entity, *required_attributes):
        if not isinstance(entity, Entity):
            raise ComponentError(f'Attempted to attach component {self} to non-entity object {entity}')
        for attr in required_attributes:
            if not hasattr(entity, attr):
                if not entity.components.get(attr):
                    raise ComponentError(f'Component {self} cannot be attached to {entity} without attribute {attr}')
        self.entity = entity
