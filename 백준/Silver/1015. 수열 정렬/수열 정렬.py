N = int(input())
A = list(map(int, input().split()))
sorted_A = sorted(A)

result = []
for i in range(N):
    idx = sorted_A.index(A[i])
    result.append(idx)
    sorted_A[idx] = -1

print(*result)