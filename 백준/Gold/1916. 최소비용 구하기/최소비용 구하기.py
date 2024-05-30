import heapq
import sys

def dijkstra(start):
    heap = []
    heapq.heappush(heap, (0, start))    # 시작 도시의 최소 비용은 0
    distance[start] = 0

    while heap:
        dist, now = heapq.heappop(heap)

        if distance[now] < dist:
            continue

        for next_city, next_cost in bus[now]:
            cost = dist + next_cost

            if cost < distance[next_city]:
                distance[next_city] = cost
                heapq.heappush(heap, (cost, next_city))

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    bus[start].append((end, cost))

start_city, end_city = map(int, sys.stdin.readline().split())

# 최소 비용을 저장할 리스트
distance = [float('inf')] * (N + 1)

dijkstra(start_city)

print(distance[end_city])