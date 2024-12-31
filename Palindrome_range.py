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


print(palindrome_range(1, 250))

