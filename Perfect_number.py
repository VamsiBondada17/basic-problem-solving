def factors_sum(num):
    summ = 0
    for i in range(1, num):
        if num % i == 0:
            summ += i
    return summ


def is_perfect_num(num):
    if num == factors_sum(num):
        return True
    else:
        return False


print(is_perfect_num(28))