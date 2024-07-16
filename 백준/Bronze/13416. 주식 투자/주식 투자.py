import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())

    total = 0
    idx = -1
    for _ in range(N):
        abc = list(map(int, input().split()))
        max_abc = max(abc)
        if max_abc > 0:
            total += max_abc

    print(total)