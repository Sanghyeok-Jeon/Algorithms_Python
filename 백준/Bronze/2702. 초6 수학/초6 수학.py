def gcd(a, b):
    return gcd(b%a, a) if b%a else a

T = int(input())
for tc in range(T):
    a, b = map(int, input().split())
    LCM, GCD = 0, 0

    if a > b:
        a, b = b, a

    GCD = gcd(a, b)
    LCM = a * b // GCD

    print(LCM, GCD)