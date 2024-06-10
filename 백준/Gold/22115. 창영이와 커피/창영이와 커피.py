import sys
input = sys.stdin.readline

N, K = map(int, input().split())
caffeine_levels = list(map(int, input().split()))

# dp[x]는 카페인 x를 얻기 위해 필요한 최소 커피 개수
dp = [101] * (100000 + 1)
dp[0] = 0  # 0mg 카페인을 얻기 위해 필요한 커피는 0개

length = 0
for caffeine in caffeine_levels:
    for j in range(length + caffeine, caffeine - 1, -1):
        dp[j] = min(dp[j], dp[j - caffeine] + 1)
    length += caffeine

# 결과 출력
if dp[K] == 101:
    print(-1)
else:
    print(dp[K])