N, K = map(int, input().split())
data = list(map(int, input().split()))

max_sum = -100 * 100
for i in range(N - K + 1):
    max_sum = max(max_sum, sum(data[i:i+K]))

print(max_sum)