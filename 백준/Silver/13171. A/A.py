import sys
input = sys.stdin.readline

def modular_exponentiation(a, x, mod):
    result = 1
    base = a % mod

    while x > 0:
        if x % 2 == 1:
            result = (result * base) % mod

        base = (base * base) % mod
        x //= 2

    return result

A = int(input())
X = int(input())
MOD = 10 ** 9 + 7

print(modular_exponentiation(A, X, MOD))