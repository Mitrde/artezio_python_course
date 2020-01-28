def old_range(*args):
    if len(args) == 1:
        return list(range(args[0]))
    elif len(args) == 2:
        return list(range(args[0], args[1]))
    elif len(args) ==3:
        return list(range(args[0], args[1], args[2]))



