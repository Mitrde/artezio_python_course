def foo(*args, **kwargs):
    """function takes list, tuple or dict and returns product and sum of elements"""
    flatten_list = []
    if args in args:
        return None

    def rec_count_sum(*items):
        """recursively adds elements to flatten list"""
        args = items[0]
        for arg in args:
            if args in args:
                flatten_list.append("error")
                return None
            if isinstance(arg, (list, tuple)):
                rec_count_sum(arg)
            else:
                flatten_list.append(arg)

    for arg in args:
        if isinstance(arg, (list, tuple)):
            rec_count_sum(arg)
        else:
            flatten_list.append(arg)

    for kwarg in kwargs.values():
        if isinstance(kwarg, (list, tuple)):
            rec_count_sum(kwarg)
        else:
            flatten_list.append(kwarg)

    if "error" in flatten_list:
        print("Data contains a circular reference!")
        return None
    elem_sum = sum(flatten_list)
    elem_mult = 1
    for elem in flatten_list:
        if elem != 0:
            elem_mult *= elem

    return elem_mult, elem_sum
