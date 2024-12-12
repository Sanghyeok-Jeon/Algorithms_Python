A, B = input().split()
N = len(A)
M = len(B)
cw = [['.'] * N for _ in range(M)]

for i in range(N):
    if A[i] in B:
        r = i
        c = B.index(A[i])
        break

for i in range(M):
    cw[i][r] = B[i]
for i in range(N):
    cw[c][i] = A[i]

for i in cw:
    print(''.join(i))