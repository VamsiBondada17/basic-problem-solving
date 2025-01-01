from math import sqrt


def is_perfect_square(num):
    sr = int(sqrt(num))
    if num == sr * sr:
        return True
    else:
        return False


print(is_perfect_square(81))


