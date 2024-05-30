import sys

N, M = map(int, input().split())
number = list(map(int, sys.stdin.readline().split()))

prefixSum = [0]
tmpSum = 0
for num in number:
    tmpSum += num
    prefixSum.append(tmpSum)

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(prefixSum[j] - prefixSum[i-1])