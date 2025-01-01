def sum_of_digit(num):
    summ = 0
    while num != 0:
        rem = num % 10
        summ += rem
        num = num // 10
    return summ


def is_harshad_number(num):
    if num % sum_of_digit(num) == 0:
        return 'Its an harshad number'
    else:
        return 'Its not an harshad number'


print(is_harshad_number(21))

