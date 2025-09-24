import sys

input = sys.stdin.buffer.readline

N, Q = map(int, input().split())
A = [0] + sorted(list(map(int, input().split())))
A_sum = [0]
for i in range(1, N + 1):
    A_sum.append(A_sum[i - 1] + A[i])

for _ in range(Q):
    L, R = map(int, input().split())
    print(A_sum[R] - A_sum[L - 1])