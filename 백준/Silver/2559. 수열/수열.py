N, K = map(int, input().split())
data = list(map(int, input().split()))

max_sum = prev_sum = sum(data[:K])
for i in range(K, N):
    now_sum = prev_sum - data[i - K] + data[i]
    max_sum = max(max_sum, now_sum)
    prev_sum = now_sum

print(max_sum)