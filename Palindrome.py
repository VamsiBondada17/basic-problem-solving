def reverse(num):
    org = num
    rem = 0
    rev = 0
    while num != 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10
    return rev


def is_palindrome(num):
    if num == reverse(num):
        return True
    else:
        return False


print(is_palindrome(555))

