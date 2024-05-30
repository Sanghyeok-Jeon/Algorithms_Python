from collections import deque
import sys
input = sys.stdin.readline

# 구슬을 이동시키는 함수
def move(board, x, y, dx, dy):
    count = 0    # 이동 횟수

    while board[x + dx][y + dy] != '#' and board[x][y] != 'O':
        x += dx
        y += dy
        count += 1

    return x, y, count

# BFS 통해 구슬 이동을 탐색하는 함수
def bfs(board, rx, ry, bx, by):
    q = deque([(rx, ry, bx, by, 1)])
    visited = set([(rx, ry, bx, by)])    # 방문한 상태 저장하는 집합

    while q:
        rx, ry, bx, by, cnt = q.popleft()

        # 이동 횟수가 10번을 초과할 경우
        if cnt > 10:
            break
        
        # 상하좌우로 구슬 이동
        for i in range(4):
            nrx, nry, rCnt = move(board, rx, ry, dx[i], dy[i])    # 빨간 구슬 이동
            nbx, nby, bCnt = move(board, bx, by, dx[i], dy[i])    # 파란 구슬 이동

            if board[nbx][nby] != 'O':    # 파란 구슬이 구멍에 빠지지 않은 경우
                if board[nrx][nry] == 'O':    # 빨간 구슬이 구멍에 빠진 경우
                    return cnt

                if (nrx, nry) == (nbx, nby):    # 두 구슬이 같은 위치에 놓일 경우 이동거리를 비교하여 더 멀리 있던 구슬을 한 칸 뒤로 이동시킴
                    if rCnt > bCnt:    # 빨간 구슬이 더 멀리 있었던 경우
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:              # 파란 구슬이 더 멀리 있었던 경우
                        nbx -= dx[i]
                        nby -= dy[i]

                if (nrx, nry, nbx, nby) not in visited:    # 빨간 구슬과 파란 구슬이 방문하지 않은 상태인 경우
                    q.append((nrx, nry, nbx, nby, cnt + 1))
                    visited.add((nrx, nry, nbx, nby))

    return -1    # 빨간 구슬이 구멍에 도달하지 못한 경우


N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

rx, ry, bx, by = 0, 0, 0, 0    # 빨간 구슬, 파란 구슬의 초기 위치
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            rx, ry = i, j
        elif board[i][j] == 'B':
            bx, by = i, j

# 상, 하, 좌, 우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 최소 이동 횟수 구하기
result = bfs(board, rx, ry, bx, by)

print(result)