def is_on_ground(collider, terrain):
    entity_footprint = collider.copy()
    entity_footprint.left += (collider.width / 12)
    entity_footprint.width -= (collider.width / 12)
    entity_footprint.top += collider.height
    entity_footprint.height = 2
    ret = entity_footprint.collidelist(terrain)
    if ret == -1:
        return False
    else:
        return True
