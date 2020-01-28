t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
s = [1, 2, 3]


def difference_between_two_lists(first, second):
    return list(set(first) - set(second))


print(difference_between_two_lists(t, s))
