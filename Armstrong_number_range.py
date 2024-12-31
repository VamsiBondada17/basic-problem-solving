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


def armstrong_number_range(num1, num2):
    numbers = []
    for i in range(num1, num2 + 1):
        if is_armstrong(i):
            numbers.append(i)
    return numbers


print(armstrong_number_range(1, 1000))

