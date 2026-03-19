import sys

k = int(sys.stdin.readline())

limit = 8000000

is_prime = [True] * (limit + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(limit ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, limit + 1, i):
            is_prime[j] = False

count = 0
for i in range(2, limit + 1):
    if is_prime[i]:
        count += 1
        if count == k:
            print(i)
            break