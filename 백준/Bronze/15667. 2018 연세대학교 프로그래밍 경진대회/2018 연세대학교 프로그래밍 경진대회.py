N = int(input())
for i in range(N):
    if i*(i+1) == N-1:
        K = i
        break

print(K)