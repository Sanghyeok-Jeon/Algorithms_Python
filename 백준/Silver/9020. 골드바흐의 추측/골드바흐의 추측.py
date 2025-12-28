import sys
input = sys.stdin.readline

MAX = 10000

is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX + 1, i):
            is_prime[j] = False

t = int(input())

for _ in range(t):
    n = int(input())
    a = b = n // 2

    while a > 0:
        if is_prime[a] and is_prime[b]:
            print(a, b)
            break
        a -= 1
        b += 1