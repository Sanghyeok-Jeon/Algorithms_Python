N, M = map(int, input().split())

basket = [0] * N
for _ in range(M):
    i, j, k = map(int, input().split())
    for n in range(i-1, j):
        basket[n] = k

print(*basket)