def foo(first_num, second_num, third_num, fourth_num):
    """function takes for numbers and returns average and maximum of all calls"""
    foo.maximum = vars(foo).setdefault("maximum", first_num)

    foo.maximum = max(first_num, second_num, third_num, fourth_num, foo.maximum)
    average = (first_num + second_num + third_num + fourth_num) / 4
    return average, foo.maximum


print(foo(2, 5, 10, 3))

print(foo(2, 5, 17, 3))
