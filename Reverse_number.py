def reversed_number(num):
    rem = 0
    rev = 0
    while num != 0:
        rem = num % 10
        rev = 10 * rev + rem
        num = num // 10
    return rev


print(reversed_number(501))
