def factors_sum(num):
    summ = 0
    for i in range(1, num):
        if num % i == 0:
            summ += i
    return summ


def is_abudant_number(num):
    if factors_sum(num) > num:
        return "Its an Abundant number"
    else:
        return "Not an Abundant number"


print(is_abudant_number(12))

