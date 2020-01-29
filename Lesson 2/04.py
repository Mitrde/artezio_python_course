def old_range(*args):
    it = 0
    step = 1
    tmp_list = []
    if len(args) == 1:
        while it < args[0]:
            tmp_list.append(it)
            it += step
        return tmp_list
    elif len(args) == 2:
        it = args[0]
        while it < args[1]:
            tmp_list.append(it)
            it += step
        return tmp_list
    elif len(args) == 3:
        it = args[0]
        step = args[2]
        while it < args[1]:
            tmp_list.append(it)
            it += step
        return tmp_list
