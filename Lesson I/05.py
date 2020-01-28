firstSet = set([1, 2])
secondSet = set([3, 4])

thirdSet = set([5])


def is_subset(first, second, third):
    return third.issubset(first) and third.issubset(second)


print(is_subset(firstSet, secondSet, thirdSet))
