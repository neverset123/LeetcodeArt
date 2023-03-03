def isLongPressedName(self, name, typed):
    from itertools import groupby
    name_groups = [(ch, len(list(g))) for ch, g in groupby(name)]
    typed_groups = [(ch, len(list(g))) for ch, g in groupby(typed)]
    if len(typed_groups) < len(name_groups):
        return False
    for i in range(len(name_groups)):
        if typed_groups[i][0] != name_groups[i][0] or \
            typed_groups[i][1] < name_groups[i][1]:
            return False
    return True