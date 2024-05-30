import sys
input = sys.stdin.readline

def dfs(idx, visited):
    if idx == N:    # 모든 일을 다 처리한 경우
        return 0

    if dp[visited] != float('inf'):    # 이미 계산한 적이 있는 경우
        return dp[visited]

    for i in range(N):
        if visited & (1 << i) == 0:    # 아직 처리하지 않은 일인 경우
            dp[visited] = min(dp[visited], D[idx][i] + dfs(idx + 1, visited | (1 << i)))

    return dp[visited]

N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
dp = [float('inf')] * (1 << N)

print(dfs(0, 0))