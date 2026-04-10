import sys

input = sys.stdin.readline

n, d, k, c = map(int, input().split())
belt = [int(input()) for _ in range(n)]

belt += belt[:k - 1]

count = [0] * (d + 1)
kind = 0

for i in range(k):
    if count[belt[i]] == 0:
        kind += 1
    count[belt[i]] += 1

answer = kind + (1 if count[c] == 0 else 0)

for i in range(1, n):
    left = belt[i - 1]
    count[left] -= 1
    if count[left] == 0:
        kind -= 1

    right = belt[i + k - 1]
    if count[right] == 0:
        kind += 1
    count[right] += 1

    answer = max(answer, kind + (1 if count[c] == 0 else 0))

print(answer)