x = {'a': 1, 'b': 2}
y = {'b': 10, 'c': 11}


def merge_two_dict(first, second):
    merged_dict = first.copy()
    merged_dict.update(second)
    return merged_dict


print(merge_two_dict(x, y))
