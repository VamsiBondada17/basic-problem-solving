def deficient_num(num):
    summ = 0
    for i in range(1, num):
        if num % i == 0:
            summ += i
    return summ


def main(num):
    if num > deficient_num(num):
        return True
    else:
        return False


print(main(97))