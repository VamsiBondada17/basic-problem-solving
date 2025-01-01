def sum_of_digits(num):
    summ = 0
    while num != 0:
        rem = int(num % 10)
        summ += rem
        num = num / 10
    return summ


print(sum_of_digits(125))

