def sum_of_n_nums(num1, num2):
    summ = 0
    for i in range(num1, num2):
        summ += i
    return summ


print(sum_of_n_nums(1, 5))