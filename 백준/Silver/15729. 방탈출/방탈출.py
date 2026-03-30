import sys

input = sys.stdin.readline

n = int(input())
target = list(map(int, input().split()))

cur = [0] * n
answer = 0

for i in range(n):
    if cur[i] != target[i]:
        answer += 1
        for j in range(i, min(i + 3, n)):
            cur[j] ^= 1

print(answer)