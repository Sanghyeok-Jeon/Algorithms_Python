import sys

def DFS(x, y, direction):
    global count

    if x == N-1 and y == N-1:
        count += 1
        return

    if direction == 0:    # 파이프방향 : 가로
        if y + 1 < N and house[x][y + 1] == 0:
            DFS(x, y + 1, 0)
        if x + 1 < N and y + 1 < N and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
            DFS(x + 1, y + 1, 2)
    elif direction == 1:    # 파이프방향 : 세로
        if x + 1 < N and house[x + 1][y] == 0:
            DFS(x + 1, y, 1)
        if x + 1 < N and y + 1 < N and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
            DFS(x + 1, y + 1, 2)
    else:    # 파이프방향 : 대각선
        if y + 1 < N and house[x][y + 1] == 0:
            DFS(x, y + 1, 0)
        if x + 1 < N and house[x + 1][y] == 0:
            DFS(x + 1, y, 1)
        if x + 1 < N and y + 1 < N and house[x + 1][y] == 0 and house[x][y + 1] == 0 and house[x + 1][y + 1] == 0:
            DFS(x + 1, y + 1, 2)

N = int(sys.stdin.readline())
house = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count = 0
DFS(0, 1, 0)

print(count)