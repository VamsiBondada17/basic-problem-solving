# Basic Math Problems Documentation

## Adam Number
A number is called an Adam number if the square of the number is a permutation of the number itself.
```python
def reversed_num(num):
    rev = 0
    while num != 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num = num // 10

    return rev

def squared_num(num):
    return num**2

def main():
    num = int(input("Enter the Number: "))
    original_num = num
    rev_num = reversed_num(num)
    sq_num1 = squared_num(num)
    sq_num2 = squared_num(rev_num)
    sq_rev_num = reversed_num(sq_num2)


    if sq_num1 == sq_rev_num:
        return ("Adam")
    else:
        return ("Not")
```
## Abundant Number
A number is considered abundant if the sum of its proper divisors is greater than the number itself.

```python
def factors_sum(num):
    summ = 0
    for i in range(1, num):
        if num % i == 0:
            summ += i
    return summ


def is_abudant_number(num):
    if factors_sum(num) > num:
        return "Its an Abundant number"
    else:
        return "Not an Abundant number"
```

## Armstrong Number
An Armstrong number is a number that equals the sum of its own digits raised to the power of the number of digits.

```python
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
```

## Automorphic Number
An automorphic number is a number whose square ends with the number itself.

```python
import math


def finding_square_of_number(num):
    return num**2


def finding_last_number(num):
    rem = finding_square_of_number(num) % 10
    return rem


def is_automorphic_number(num):
    if finding_last_number(num) == num:
        return f'Its a Automorphic number'
    else:
        return f'Its not an Automorphic number'
```

## Deficient Number 

The given number which is lesser than perfect number 

```python
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


```


## Factor of a Number
Finds all factors of a given number.

```python
def finding_factors(num):
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    return factors
```

## Factorial of a Number
Calculates the factorial of a given number (n!).

```python
def finding_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial
```

## Fibonacci Number
Generates Fibonacci sequence up to n terms.

```python
def fibonacci(num):
    n1, n2 = 0, 1
    print("Fibonacci Series: ", n1, n2, end=" ")
    for i in range(2, num):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=" ")

    print()
```

## GCD (Greatest Common Divisor)
Finds the greatest common divisor of two numbers.

```python
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
```

## Harshad Number
A Harshad number is a number that is divisible by the sum of its digits.

```python
def sum_of_digit(num):
    summ = 0
    while num != 0:
        rem = num % 10
        summ += rem
        num = num // 10
    return summ


def is_harshad_number(num):
    if num % sum_of_digit(num) == 0:
        return 'Its an harshad number'
    else:
        return 'Its not an harshad number'
```

## HCF (Highest Common Factor)
Finds the highest common factor of two numbers (same as GCD).

```python
def hcf(a, b):
    while b:
        a, b = b, a % b
    return a
```

## Hello World
Printing Hello World Statement

```python
print("Hello World")
```

## LCM (Least Common Multiple)
Finds the least common multiple of two numbers.

```python
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
```

## Leap Year
Determines if a given year is a leap year.

```python
def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        return True
    else:
        return False
```

## Palindrome Number
Checks if a number reads the same forwards and backwards.

```python
def reverse(num):
    rem = 0
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev


def is_palindrome(num):
    if num < 10:
        return False
    if num == reverse(num):
        return True
    else:
        return False


def palindrome_range(num1, num2):
    palindrome = []
    for i in range(num1, num2):
        if is_palindrome(i):
            palindrome.append(i)

    return palindrome
```

## Perfect Number
A perfect number is a number that equals the sum of its proper divisors.

```python
def factors_sum(num):
    summ = 0
    for i in range(1, num):
        if num % i == 0:
            summ += i
    return summ


def is_perfect_num(num):
    if num == factors_sum(num):
        return True
    else:
        return False
```

## Perfect Square
Determines if a number is a perfect square.

```python
from math import sqrt


def is_perfect_square(num):
    sr = int(sqrt(num))
    if num == sr * sr:
        return True
    else:
        return False
```

## Power of Two
Checking the given input is Power of Two or not.

```python
def is_power_of_2(num):
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            return False
    return num == 1
```

## Prime Factors
Finds all prime factors of a number.

```python
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
```

## Prime Number
Determines if a number is prime.

```python
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
```

## Reverse of a Number
Returns the reverse of a given number.

```python
def reversed_number(num):
    rem = 0
    rev = 0
    while num != 0:
        rem = num % 10
        rev = 10 * rev + rem
        num = num // 10
    return rev
```

## Sum of Digits
Calculates the sum of digits in a number.

```python
def sum_of_digits(num):
    summ = 0
    while num != 0:
        rem = int(num % 10)
        summ += rem
        num = num / 10
    return summ
```

## Sum of N Natural Numbers
Calculates the sum of first n natural numbers.

```python
def sum_of_n_nums(num):
    summ = 0
    for i in range(1, num + 1):
        summ += i
    return summ
```

## Twin Primes
Twin primes are pairs of prime numbers that differ by 2. For example, (3, 5), (5, 7), and (11, 13) are twin prime pairs.

```python
import math


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False

    return True


for i in range(3, 100):
    if is_prime(i-2) and is_prime(i):
        print(i-2, i)
```

