import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memeory = list(map(int, input().split()))
cost = list(map(int, input().split()))

# 최대 비용
max_cost = sum(cost)

# dp[i][j] : i번째 앱까지 고려했을때, j 비용으로 확보할 수 있는 최대 메모리
dp = [[0] * (max_cost + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(max_cost + 1):
        if cost[i - 1] <= j:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i - 1]] + memeory[i - 1])
        else:
            dp[i][j] = dp[i - 1][j]

# 최소 비용 찾기
min_cost = max_cost
for j in range(max_cost + 1):
    if dp[N][j] >= M:
        min_cost = j
        break

print(min_cost)