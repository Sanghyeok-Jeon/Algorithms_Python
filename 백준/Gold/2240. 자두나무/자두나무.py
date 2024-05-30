T, W = map(int, input().split())
plums = [0] + [int(input()) for _ in range(T)]

dp = [[0] * (W+1) for _ in range(T+1)]

for i in range(1, T+1):
    # 한 번도 안 움직이는 경우(W = 0)
    if plums[i] == 1:
        dp[i][0] = dp[i-1][0] + 1
    else:
        dp[i][0] = dp[i-1][0]

    for j in range(1, W+1):
        if j > i:
            break

        if plums[i] == 1 and not j % 2:  # 1번 나무에서 떨어지는 자두 먹기
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1    # [i-1][j] : 1로 이동, [i-1][j-1] : 제자리
        elif plums[i] == 2 and j % 2:    # 2번 나무에서 떨어지는 자두 먹기
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + 1
        else:    # 안 먹는 경우
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1])

print(max(dp[T]))