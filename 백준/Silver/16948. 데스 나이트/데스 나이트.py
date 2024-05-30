import collections

def BFS():
    while q:
        for _ in range(len(q)):
            r, c, cnt = q.popleft()
            if r == r2 and c == c2:
                return cnt

            for mode in range(6):
                nr = r + dr[mode]
                nc = c + dc[mode]
                if 0 <= nr < N and 0 <= nc < N:
                    if visited[nr][nc] == 0:
                        visited[nr][nc] = 1
                        q.append((nr, nc, cnt+1))

    return -1

N = int(input())
r1, c1, r2, c2 = map(int, input().split())
q = collections.deque()
visited = [[0]*N for _ in range(N)]

dr = [-2, -2, 0, 0, 2, 2]
dc = [-1, 1, -2, 2, -1, 1]

visited[r1][c1] = 1
q.append((r1, c1, 0))

print(BFS())