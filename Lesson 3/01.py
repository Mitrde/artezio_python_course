def sqr(args):
    """ return squared numbers"""
    res = []
    for num in args:
        res.append(num*num)
    return res


def is_even(args):
    """ return even-position numbers from list"""
    res = []
    for i in range(1, len(args), 2):  # args[0] is first position(odd)
        res.append(args[i])
    return res


def cubed(args):
    """ return odd-position cubed numbers in list"""
    res = []
    for i in range(0, len(args), 2):  # args[0] is first position(odd)
        if args[i] % 2 == 0:
            res.append(args[i]**3)
    return res

