import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def DFS(node, weight):
    for w, v in graph[node]:
        if distance[v] == -1:
            distance[v] = weight + w
            DFS(v, distance[v])

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n-1):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
    graph[b].append((c, a))

distance = [-1] * (n + 1)
distance[1] = 0
DFS(1, 0)    # 루트 노드에서 가중치 합이 최대인 노드 찾기

start_node = distance.index(max(distance))    # 가중치 합이 최대인 노드
distance = [-1] * (n + 1)
distance[start_node] = 0
DFS(start_node, 0)    # 트리의 지름을 구하기 위한 DFS 재수행

print(max(distance))