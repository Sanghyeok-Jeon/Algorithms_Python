import sys
import collections

def BFS():
    max_cnt = 0
    while q:
        i, j, cnt = q.popleft()
        for mode in range(4):
            ni = i + di[mode]
            nj = j + dj[mode]
            if 0 <= ni < N and 0 <= nj < M and tomato[ni][nj] == 0:
                tomato[ni][nj] = cnt+1
                q.append((ni, nj, cnt+1))
        max_cnt = max(max_cnt, cnt)

    for x in range(N):
        if 0 in tomato[x]:
            return -1

    return max_cnt

M, N = map(int, sys.stdin.readline().split())
tomato = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
q = collections.deque()

di = [1, -1, 0, 0]
dj = [0, 0, 1, -1]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i, j, 0))

print(BFS())