my_list = [1, 2, 3, 1, 2, 5, 6, 7, 8]


def remove_duplicates(some_list):
    return list(set(some_list))


print(remove_duplicates(my_list))
