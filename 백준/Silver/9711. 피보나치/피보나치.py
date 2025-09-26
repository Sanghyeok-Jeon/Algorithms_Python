dp = [0, 1]
for i in range(2, 10001):
    dp.append(dp[i - 2] + dp[i - 1])

T = int(input())
for i in range(1, T + 1):
    P, Q = map(int, input().split())
    print('Case #{}:'.format(i), dp[P] % Q)