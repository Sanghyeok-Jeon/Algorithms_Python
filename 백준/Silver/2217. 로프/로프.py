def max_weight(ropes):
    ropes.sort(reverse=True)

    max_weight = 0
    for i in range(len(ropes)):
        weight = ropes[i] * (i + 1)
        max_weight = max(max_weight, weight)

    return max_weight

import sys
input = sys.stdin.readline

n = int(input())
ropes = [int(input()) for _ in range(n)]

print(max_weight(ropes))