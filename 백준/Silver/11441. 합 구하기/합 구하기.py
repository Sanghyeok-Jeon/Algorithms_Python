import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

list_sum = [0]
for n in range(N):
    list_sum.append(list_sum[-1] + A[n])

M = int(input())
for _ in range(M):
    i, j = map(int, input().split())
    print(list_sum[j] - list_sum[i - 1])