import sys
from collections import deque

def solve():
    input = sys.stdin.readline
    a, b = map(int, input().split())
    n, m = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    dist = [-1] * (n + 1)
    q = deque([a])
    dist[a] = 0

    while q:
        x = q.popleft()
        if x == b:
            break
        for nx in graph[x]:
            if dist[nx] == -1:
                dist[nx] = dist[x] + 1
                q.append(nx)

    print(dist[b])

if __name__ == "__main__":
    solve()