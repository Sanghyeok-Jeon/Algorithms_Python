def binomial_coefficient(n, k):
    if k > n - k:
        k = n - k
    result = 1
    for i in range(k):
        result = result * (n - i) // (i + 1)
    return result

import sys
input = sys.stdin.readline

while True:
    n, k = map(int, input().strip().split())
    if n == 0 and k == 0:
        break

    print(binomial_coefficient(n, k))