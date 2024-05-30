import sys
import collections

def DFS(v):
    global N
    visited1[v] = 1
    print(v, end=' ')

    if sum(visited1) == N:
        return

    for i in range(1, N+1):
        if graph[v][i] == 1 and visited1[i] == 0:
            visited1[i] = 1
            DFS(i)

def BFS():
    global N
    while q:
        for _ in range(len(q)):
            v = q.popleft()
            print(v, end=' ')
            if sum(visited2) == N:
                break

            for i in range(1, N+1):
                if graph[v][i] == 1 and visited2[i] == 0:
                    q.append(i)
                    visited2[i] = 1
    return

N, M, V = map(int, input().split())
graph = [[0]*(N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
q = collections.deque()
q.append(V)

visited1 = [0] * (N+1)
DFS(V)
print()
visited2 = [0] * (N+1)
visited2[V] = 1
BFS()
print()