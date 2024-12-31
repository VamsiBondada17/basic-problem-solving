def armstrong_number(num):
    digit = len(str(num))
    rem = 0
    fact = 0

    while num != 0:
        rem = num % 10
        fact += rem**digit
        num = num // 10
    return fact


def is_armstrong(num):
    if num == armstrong_number(num):
        return True
    else:
        return False


print(is_armstrong(407))


