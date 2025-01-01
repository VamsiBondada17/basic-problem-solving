import math


def finding_square_of_number(num):
    return num**2


def finding_last_number(num):
    rem = finding_square_of_number(num) % 10
    return rem


def is_automorphic_number(num):
    if finding_last_number(num) == num:
        return f'Its a Automorphic number'
    else:
        return f'Its not an Automorphic number'


print(is_automorphic_number(9))

