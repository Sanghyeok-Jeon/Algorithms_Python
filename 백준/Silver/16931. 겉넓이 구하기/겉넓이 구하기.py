import sys
input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]

answer = 0

cnt_non_zero = 0
for i in range(N):
    for j in range(M):
        if grid[i][j] > 0:
            cnt_non_zero += 1
answer += cnt_non_zero * 2

for i in range(N):
    answer += grid[i][0]
    answer += grid[i][M - 1]

    for j in range(1, M):
        diff = grid[i][j] - grid[i][j - 1]
        if diff > 0:
            answer += diff

    for j in range(M - 2, -1, -1):
        diff = grid[i][j] - grid[i][j + 1]
        if diff > 0:
            answer += diff

for j in range(M):
    answer += grid[0][j]
    answer += grid[N - 1][j]

    for i in range(1, N):
        diff = grid[i][j] - grid[i - 1][j]
        if diff > 0:
            answer += diff

    for i in range(N - 2, -1, -1):
        diff = grid[i][j] - grid[i + 1][j]
        if diff > 0:
            answer += diff

print(answer)