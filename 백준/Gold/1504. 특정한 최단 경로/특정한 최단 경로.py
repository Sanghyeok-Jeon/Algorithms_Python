import heapq
import sys

def dijkstra(start):
    distance = [float('inf')] * (N + 1)    # 시작점으로부터의 최단 거리를 저장할 리스트
    distance[start] = 0    # 시작점의 최단 거리는 0으로 초기화
    heap = []
    heapq.heappush(heap, (0, start))    # 우선순위 큐에 시작점과 최단 거리를 넣음

    while heap:
        dist, node = heapq.heappop(heap)

        if distance[node] < dist:
            continue

        for next_node, next_dist in graph[node]:
            cost = dist + next_dist

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))

    return distance

N, E = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]

for _ in range(E):
    a, b, c = map(int, sys.stdin.readline().split())    # 간선의 정보: 정점 a, 정점 b, 거리 c
    graph[a].append((b, c))    # 정점 a에서 정점 b까지의 간선 정보 추가
    graph[b].append((a, c))    # 정점 b에서 정점 a까지의 간선 정보 추가

V1, V2 = map(int, sys.stdin.readline().split())    # 반드시 지나야 하는 두 정점 V1, V2

# 1번 정점으로부터 모든 정점까지의 최단 거리 계산
dist_from_1 = dijkstra(1)

# V1과 V2를 지나는 최단 경로 계산
# 1 -> V1 -> V2 -> N
path1 = dist_from_1[V1] + dijkstra(V1)[V2] + dijkstra(V2)[N]
# 1 -> V2 -> V1 -> N
path2 = dist_from_1[V2] + dijkstra(V2)[V1] + dijkstra(V1)[N]

result = min(path1, path2)

print(result if result < float('inf') else -1)