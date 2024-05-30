N = int(input())
dp = [0] * (N+1)  # 상근 승 : 1, 창영 승 : 0

for i in range(1, N+1):
    if i == 1:
        dp[i] = 0
    elif i == 2:
        dp[i] = 1
    elif i == 3:
        dp[i] = 0
    elif i == 4:
        dp[i] = 1
    else:
        dp[i] = 0 if dp[i-1] and dp[i-3] and dp[i-4] else 1

print('SK' if dp[N] else 'CY')