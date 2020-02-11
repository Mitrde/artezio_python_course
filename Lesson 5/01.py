""" Module with complex number class"""


class Complex:
    """Complex number class"""

    def __init__(self, re, im=0.0):
        self.__re = re
        self.__im = im

    @staticmethod
    def return_format(real, image):
        """"returns appropriate complex number style"""
        if image >= 0:
            return '{:.2f}+{:.2f}i'.format(real, image)
        return '{:.2f}{:.2f}i'.format(real, image)

    def __add__(self, other):
        real = self.__re + other.__re
        image = self.__im + other.__im
        return Complex.return_format(real, image)

    def __sub__(self, other):
        real = self.__re - other.__re
        image = self.__im - other.__im
        return Complex.return_format(real, image)

    def __mul__(self, other):
        real = self.__re * other.__re - self.__im * other.__im
        image = self.__re * other.__im + self.__im * other.__re
        return Complex.return_format(real, image)

    def __truediv__(self, other):
        real = (self.__re * other.__re + self.__im * other.__im) / (other.__re ** 2 + other.__im ** 2)
        image = (self.__im * other.__re - self.__re * other.__im) / (other.__re ** 2 + other.__im ** 2)
        return Complex.return_format(real, image)

    def __abs__(self):
        return '{:.2f}+0.00i'.format((self.__re ** 2 + self.__im ** 2) ** (1 / 2))

    def __str__(self):
        return Complex.return_format(self.__re, self.__im)


def mod(complex_num):
    """ Returns complex number abs"""
    return abs(complex_num)


C = Complex(*list(map(float, input().split())))
D = Complex(*list(map(float, input().split())))

print(C + D)
print(C - D)
print(C * D)
print(C/D)
print(mod(C))
print(mod(D))


