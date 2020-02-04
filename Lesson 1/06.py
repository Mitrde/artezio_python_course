n = int(input())


def make_dict(num):
    tmp_dict = dict()

    for i in range(1, num):
        tmp_dict[i] = i*i
    return tmp_dict


print(make_dict(n))

