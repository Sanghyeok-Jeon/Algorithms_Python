T = int(input())

result = []
for tc in range(T):
    N = int(input())
    dp = [[0, 0]]*(N+1)

    for i in range(N+1):
        if i == 0:
            dp[i] = [1, 0]
        elif i == 1:
            dp[i] = [0, 1]
        else:
            dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]
    result.append('{} {}'.format(dp[N][0], dp[N][1]))
print(*result, sep='\n')