import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    factor = 2
    result = []

    while factor * factor <= n:
        cnt = 0
        while n % factor == 0:
            n //= factor
            cnt += 1
        if cnt > 0:
            result.append((factor, cnt))
        factor += 1

    if n > 1:
        result.append((n, 1))

    for p, c in result:
        print(p, c)
