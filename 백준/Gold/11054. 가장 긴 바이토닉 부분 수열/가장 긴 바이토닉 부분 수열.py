import sys
N = int(input())
A = list(map(int, sys.stdin.readline().split()))
B = A[::-1]

LIS = [1] * N
LDS = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            LIS[i] = max(LIS[i], LIS[j] + 1)
        if B[i] > B[j]:
            LDS[i] = max(LDS[i], LDS[j] + 1)

result = []
for a, b in zip(LIS, LDS[::-1]):
    result.append(a + b)

print(max(result) - 1)