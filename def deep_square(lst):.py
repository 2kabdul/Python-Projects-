def deep_square(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1 and type(lst[0]) == int:
        return [lst[0] * lst[0]]
    elif len(lst) == 1 and type(lst[0]) == list:
        return [deep_square(lst[0])] 
    elif type(lst[0]) == int:
        return [lst[0] * lst[0]] + deep_square(lst[1:])
    else:
        return [deep_square(lst[0])] + deep_square(lst[1:])