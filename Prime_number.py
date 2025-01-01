def checking_prime(num):
    count = 0
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            count = 1
            break

    if count == 1:
        return f"{num} is not Prime Number"
    else:
        return f"{num} is  a Prime number"


print(checking_prime(131))
