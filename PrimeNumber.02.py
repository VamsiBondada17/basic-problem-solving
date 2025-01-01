import math


def is_prime_number(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(math.sqrt(num))+1, 2):
        if num % i == 0:
            return False
    return True


def prime_number_range(num1, num2):
    primes = []
    for j in range(num1, num2 + 1):
        if is_prime_number(j):
            primes.append(j)
    return primes


print("Prime Numbers Count ::", len(prime_number_range(1, 100)))
print("Prime Numbers ::", prime_number_range(1, 100))
