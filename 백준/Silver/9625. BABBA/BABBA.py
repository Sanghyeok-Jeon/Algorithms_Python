K = int(input())
A = [1, 0]
B = [0, 1]

for i in range(2, K+1):
    A.append(A[i-2] + A[i-1])
    B.append(B[i-2] + B[i-1])

print(A[K], B[K])