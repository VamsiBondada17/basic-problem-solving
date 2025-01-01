import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def finding_prime_factors(num):
    prime_factors = []
    for i in range(2, num):
        if num % i == 0:
            if is_prime(i):
                prime_factors.append(i)
    return prime_factors


print(finding_prime_factors(48))

