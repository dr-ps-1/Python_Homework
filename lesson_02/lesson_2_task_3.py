import math


def square(side):
    area = side * side

    return math.ceil(area)


print("Площадь квадрата со стороной 2:", square(2))


print("Площадь квадрата со стороной 8.1:", square(8.1))
