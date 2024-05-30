N, M = map(int, input().split())

basket = list(range(1, N+1))
for _ in range(M):
    i, j = map(int, input().split())
    for n in range(i, (j+i)//2+1):
        basket[n-1], basket[i+j-n-1] = basket[i+j-n-1], basket[n-1]

print(*basket)