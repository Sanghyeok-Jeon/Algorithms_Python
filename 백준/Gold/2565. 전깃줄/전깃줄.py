import sys
input = sys.stdin.readline

N = int(input())
wire = [tuple(map(int, input().split())) for _ in range(N)]

wire.sort()
dp = [1] * N    # idx까지 교차 없이 연결 가능한 전깃줄 개수

for i in range(1, N):    # A 전봇대 번호
    for j in range(i):    # i 이전에 있는 A 전봇대 번호
        if wire[j][1] < wire[i][1]:    # i의 B 전봇대 연결번호가 j의 B 전봇대 연결번호보다 큰 경우
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))    # 전체에서 최장 증가 수열 개수 뺌