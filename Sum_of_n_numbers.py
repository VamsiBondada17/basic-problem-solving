def sum_of_n_nums(num):
    summ = 0
    for i in range(1, num + 1):
        summ += i
    return summ


print(sum_of_n_nums(10))