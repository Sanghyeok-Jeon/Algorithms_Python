N, M = map(int, input().split())
basket = list(range(1, N+1))
for _ in range(M):
    i, j, k = map(int, input().split())
    i, j, k = i-1, j-1, k-1
    basket = basket[:i] + basket[k:j+1] + basket[i:k] + basket[j+1:]

print(*basket)