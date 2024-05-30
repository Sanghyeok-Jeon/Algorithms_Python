from collections import deque
import sys

input = sys.stdin.readline
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start):
    global answer
    q = deque()
    q.append(start)

    while q:
        x, y = q.popleft()

        for mode in range(4):
            nx = x + dx[mode]
            ny = y + dy[mode]

            if 0 <= nx < h and 0 <= ny < w and board[nx][ny] != '*' and not visited[nx][ny]:    # 방문 가능한 경우
                if board[nx][ny].isupper():     # 문
                    if board[nx][ny].lower() in keys:    # 열쇠가 있는 경우
                        q.append([nx, ny])
                        visited[nx][ny] = True
                    else:     # 열쇠가 없는 경우
                        if board[nx][ny] in doors:
                            doors[board[nx][ny]].append([nx, ny])
                        else:
                            doors[board[nx][ny]] = [[nx, ny]]
                else:
                    q.append([nx, ny])
                    visited[nx][ny] = True

                    if board[nx][ny] == '$':    # 문서인 경우
                        answer += 1

                    if board[nx][ny].islower():    # 열쇠인 경우
                        keys.add(board[nx][ny])
                        if board[nx][ny].upper() in doors:
                            for door_x, door_y in doors[board[nx][ny].upper()]:    # 열쇠로 열 수 있는 곳 방문
                                q.append([door_x, door_y])
                                visited[nx][ny] = True

T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    board = [list(input()) for _ in range(h)]
    keys = set(input())
    doors = dict()
    visited = [[False] * w for _ in range(h)]

    answer = 0
    start = []
    for i in range(h):
        for j in range(w):
            if i == 0 or i == h-1 or j == 0 or j == w-1:    # 테두리
                if board[i][j] != '*':    # 벽이 아닌 경우
                    if board[i][j].isupper():    # 문인 경우
                        if board[i][j] in doors:
                            doors[board[i][j]].append([i, j])
                        else:
                            doors[board[i][j]] = [[i, j]]
                    else:
                        if board[i][j] == '$':    # 문서인 경우
                            answer += 1
                        elif board[i][j].islower():    # 열쇠인 경우
                            keys.add(board[i][j])

                        start.append([i, j])    # 시작 위치 저장
                        visited[i][j] = True

    for key in keys:     # 현재 가지고 있는 열쇠로 열 수 있는 문 좌표 탐색
        if key.upper() in doors:
            for x, y in doors[key.upper()]:
                start.append([x, y])
                visited[x][y] = True

    for s in start:    # 시작 위치에서 탐색 시작
        bfs(s)

    print(answer)