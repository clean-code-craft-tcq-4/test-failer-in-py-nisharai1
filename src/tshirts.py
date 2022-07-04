
def size(cms):
    if cms not in range(15, 50):
        return None
    if cms <= 38:
        return 'S'
    elif 38 < cms <= 42:
        return 'M'
    else:
        return 'L'
