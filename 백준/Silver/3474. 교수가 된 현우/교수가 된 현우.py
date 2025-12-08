def count_trailing_zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    print(count_trailing_zeros(n))