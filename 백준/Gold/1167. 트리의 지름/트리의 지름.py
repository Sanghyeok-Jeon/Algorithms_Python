import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def DFS(node, weight):
    for w, v in graph[node]:
        if distance[v] == -1:
            distance[v] = weight + w
            DFS(v, distance[v])

V = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(V):
    data = list(map(int, input().split()))
    a = data[0]
    i = 1
    while True:
        if data[i] == -1:
            break

        graph[a].append((data[i+1], data[i]))

        i += 2

distance = [-1] * (V + 1)
distance[1] = 0
DFS(1, 0)    # 임의의 노드(여기선 1번)에서 가장 멀리 있는 노드 찾기

start_node = distance.index(max(distance))    # 임의의 점에서 가장 멀리 있는 노드
distance = [-1] * (V + 1)
distance[start_node] = 0
DFS(start_node, 0)    # 여기서 또 가장 멀리 있는 노드를 찾으면 거기가 지름이 될 것

print(max(distance))