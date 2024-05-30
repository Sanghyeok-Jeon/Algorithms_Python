import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
M = int(input())
questions = [list(map(int, input().split())) for _ in range(M)]

dp = [[0] * (N + 1) for _ in range(N + 1)]    # dp[i][j] : i~j까지 선택했을 때, 팰린드롬인지

# 길이 1짜리
for i in range(N):
    dp[i][i] = 1

# 길이 2짜리 : 두 값이 같아야 됨.
for i in range(N-1):
    if nums[i] == nums[i+1]:
        dp[i][i+1] = 1

# 길이 3 이상 : 양 끝 값이 같아야 되고 그 사이 값들이 팰린드롬이어야 됨
for i in range(2, N):
    for j in range(N-i):
        if nums[j] == nums[j+i] and dp[j+1][j+i-1] == 1:
            dp[j][j+i] = 1

for S, E in questions:
    print(dp[S-1][E-1])