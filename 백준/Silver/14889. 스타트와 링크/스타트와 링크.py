import sys

def backTracking(idx, cnt):
    global min_diff, N

    if idx == N:
        return

    if cnt == N // 2:
        team_start, team_link = 0, 0
        for i in range(N-1):
            for j in range(i+1, N):
                if player[i] and player[j]:
                    team_start += S[i][j] + S[j][i]
                if not player[i] and not player[j]:
                    team_link += S[i][j] + S[j][i]
        min_diff = min(min_diff, abs(team_start - team_link))
        return

    player[idx] = 1
    backTracking(idx+1, cnt+1)
    player[idx] = 0
    backTracking(idx+1, cnt)

N = int(input())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
player = [0] * N
min_diff = 100 * 20 * 20

backTracking(0, 0)

print(min_diff)