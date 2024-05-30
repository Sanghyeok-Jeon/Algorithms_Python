def gcd(x, y):
    while y:
        x, y = y, x%y
    return x

a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

numerator = a1*b2 + a2*b1
denominator = b1*b2

g = gcd(numerator, denominator)

print(numerator//g, denominator//g)