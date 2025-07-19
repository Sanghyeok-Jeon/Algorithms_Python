import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

result = [0]
min_data = A[0]
max_diff = 0
for i in range(1, N):
    max_diff = max(max_diff, A[i] - min_data)
    result.append(max_diff)
    min_data = min(min_data, A[i])

print(*result)