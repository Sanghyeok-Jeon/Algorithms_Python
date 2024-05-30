import sys
import collections

def BFS():
    global next_i, next_j, I
    while q:
        i, j = q.popleft()
        if i == next_i and j == next_j:
            return visited[next_i][next_j]-1
        for mode in range(8):
            ni = i + di[mode]
            nj = j + dj[mode]
            if 0 <= ni < I and 0 <= nj < I and visited[ni][nj] == 0:
                q.append((ni, nj))
                visited[ni][nj] = visited[i][j] + 1

T = int(input())

for _ in range(T):
    I = int(input())
    now_i, now_j = map(int, sys.stdin.readline().split())
    next_i, next_j = map(int, sys.stdin.readline().split())

    visited = [[0] * I for _ in range(I)]
    q = collections.deque()
    q.append((now_i, now_j))
    visited[now_i][now_j] = 1

    di = [-2, -1, 1, 2, 2, 1, -1, -2]
    dj = [1, 2, 2, 1, -1, -2, -2, -1]

    if now_i == next_i and now_j == next_j:
        print(0)
    else:
        print(BFS())