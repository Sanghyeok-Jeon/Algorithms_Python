import sys
sys.setrecursionlimit(10**6)

def DFS(parent):
    for child in graph[parent]:
        if visited[child] == 0:
            visited[child] = parent
            DFS(child)

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N + 1)

DFS(1)

print(*visited[2:], sep='\n')
