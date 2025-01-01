def finding_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial


def strong_number(num):
    rem = 0
    digit_fact = 0
    while num != 0:
        rem = num % 10
        digit_fact += finding_factorial(rem)
        num = num // 10
    return digit_fact


def is_strong_number(num):
    if num == strong_number(num):
        return True
    else:
        return False


print(is_strong_number(145))