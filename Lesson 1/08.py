example_dict = {"aaa": 13, "ss": 3, "dd": 6, "lddd": 11, "vhgavb": 39}


def highest_3_values(some_dict):
    return list(sorted(some_dict.values()))[-3:]


print(highest_3_values(example_dict))
