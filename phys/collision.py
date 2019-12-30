def copy_faces(to_copy):
    """ Returns a dictionary containing the 4 faces of a PyGame rect """
    faces = {}

    t_rect = to_copy.copy()
    t_rect.height = 1
    t_rect.left += (t_rect.width / 15)
    t_rect.width -= ((t_rect.width / 15) * 2)
    faces['top'] = t_rect

    b_rect = to_copy.copy()
    b_rect.top += b_rect.height - 1
    b_rect.height = 1
    b_rect.left += (b_rect.width / 15)
    b_rect.width -= ((b_rect.width / 15) * 2)
    faces['bot'] = b_rect

    l_rect = to_copy.copy()
    l_rect.top += (l_rect.height / 15)
    l_rect.height -= ((l_rect.height / 15) * 2)
    l_rect.width = 1
    faces['left'] = l_rect

    r_rect = to_copy.copy()
    r_rect.top += (r_rect.height / 15)
    r_rect.height -= ((r_rect.height / 15) * 2)
    r_rect.left += (r_rect.width - 2)
    r_rect.width = 1
    faces['right'] = r_rect

    return faces


def is_on_ground(collider, terrain):
    if copy_faces(collider).get('bot').collidelist(terrain) == -1:
        return False
    else:
        return True
