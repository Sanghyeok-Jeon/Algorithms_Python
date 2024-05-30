N = int(input())
dp = [0] * (N+1)  # 상근 승 : 1, 창영 승 : 0

for i in range(1, N+1):
    if i == 1:
        dp[i] = 0
    elif i == 2:
        dp[i] = 1
    elif i == 3:
        dp[i] = 0
    else:
        dp[i] = 1 if dp[i-1] == 0 or dp[i-3] == 0 else 0

print('SK' if dp[N] else 'CY')