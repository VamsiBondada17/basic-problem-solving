import math


def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True


def check_primes_in_range(num1, num2):
    primes = []
    for num in range(num1, num2 + 1):
        if is_prime(num):
            primes.append(num)
    return primes


prime_nums = check_primes_in_range(2, 100)
print("primes count :: ", len(prime_nums))
print("prime numbers :: ", prime_nums)
