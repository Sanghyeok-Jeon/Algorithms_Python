import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def move(start, end):
    if start == end:
        return 1
    elif start == 0:
        return 2
    elif abs(start - end) == 1 or abs(start - end) == 3:
        return 3
    else:
        return 4

arr = list(map(int, input().split()))
arr.pop()
INF = int(1e9)

dp = [[[INF] * 5 for _ in range(5)] for _ in range(len(arr) + 1)]
dp[0][0][0] = 0

for i, next in enumerate(arr, start=1):
    # 왼발이 다음으로 이동
    for r in range(5):
        for l in range(5):
            dp[i][next][r] = min(dp[i][next][r], dp[i-1][l][r] + move(l, next))

    # 오른발이 다음으로 이동
    for l in range(5):
        for r in range(5):
            dp[i][l][next] = min(dp[i][l][next], dp[i-1][l][r] + move(r, next))

print(min(list(map(min, dp[len(arr)]))))