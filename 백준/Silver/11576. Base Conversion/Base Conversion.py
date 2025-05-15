def base_conversion(A, B, digits):
    decimal_value = 0
    for i, digit in enumerate(reversed(digits)):
        decimal_value += digit * (A ** i)

    if decimal_value == 0:
        return [0]

    b_base_digits = []
    while decimal_value > 0:
        b_base_digits.append(decimal_value % B)
        decimal_value //= B

    return b_base_digits[::-1]

A, B = map(int, input().split())
m = int(input())
digits = list(map(int, input().split()))

result = base_conversion(A, B, digits)
print(' '.join(map(str, result)))