import sys
import collections

def BFS():
    max_cnt = 0
    while q:
        z, y, x, cnt = q.popleft()
        for mode in range(6):
            nz = z + dz[mode]
            ny = y + dy[mode]
            nx = x + dx[mode]
            if 0 <= nz < H and 0 <= ny < N and 0 <= nx < M and tomato[nz][ny][nx] == 0:
                tomato[nz][ny][nx] = cnt + 1
                q.append((nz, ny, nx, cnt+1))
        max_cnt = max(max_cnt, cnt)

    for h in range(H):
        for n in range(N):
            if 0 in tomato[h][n]:
                return -1

    return max_cnt

M, N, H = map(int, sys.stdin.readline().split())
q = collections.deque()
tomato = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]

dy = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato[h][n][m] == 1:
                q.append((h, n, m, 0))

print(BFS())