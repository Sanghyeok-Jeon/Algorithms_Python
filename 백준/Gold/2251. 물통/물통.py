import sys
import collections

def BFS():
    global A, B, C
    while q:
        a, b, c = q.popleft()
        if not visited[a][b]:
            visited[a][b] = 1
            if not a:
                possible.append(c)

            if a + b < B:
                q.append((0, a+b, c))
            else:
                q.append((a+b-B, B, c))

            if a + c < C:
                q.append((0, b, a+c))
            else:
                q.append((a+c-C, b, C))

            if b + a < A:
                q.append((a+b, 0, c))
            else:
                q.append((A, a+b-A, c))

            if b + c < C:
                q.append((a, 0, b+c))
            else:
                q.append((a, b+c-C, C))

            if c + a < A:
                q.append((c+a, b, 0))
            else:
                q.append((A, b, c+a-A))

            if c + b < B:
                q.append((a, c+b, 0))
            else:
                q.append((a, B, c+b-B))

A, B, C = map(int, sys.stdin.readline().split())
q = collections.deque()
possible = []
visited = [[0]*(B+1) for _ in range(A+1)]
q.append((0, 0, C))

BFS()

possible.sort()
print(*possible)