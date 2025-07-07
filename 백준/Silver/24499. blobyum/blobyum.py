N, K = map(int, input().split())
cake = list(map(int, input().split()))
sum_taste = sum(cake[:K])

result = sum_taste
for i in range(K, N + K):
    ni = i % N

    sum_taste += cake[ni]
    sum_taste -= cake[ni - K]

    result = max(result, sum_taste)

print(result)