import heapq
import sys

def dijkstar(start):
    distance = [float('inf')] * (V + 1)
    distance[start] = 0
    heap = []
    heapq.heappush(heap, (0, start))

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

V, E = map(int, sys.stdin.readline().split())
K = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]
for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().split())
    graph[u].append((v, w))

dist_from_K = dijkstar(K)
for i in range(1, V+1):
    print(dist_from_K[i] if dist_from_K[i] != float('inf') else 'INF')