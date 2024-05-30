import heapq
import sys

def dijkstra(start):
    heap = []
    distance[start] = 0
    path[start] = [start]
    heapq.heappush(heap, (0, start, [start]))  # 시작 도시의 최소 비용은 0

    while heap:
        dist, now_city, now_path = heapq.heappop(heap)

        if distance[now_city] < dist:
            continue

        for next_city, next_cost in bus[now_city]:
            cost = dist + next_cost

            if cost < distance[next_city]:
                distance[next_city] = cost
                path[next_city] = now_path + [next_city]    # 경로 갱신
                heapq.heappush(heap, (cost, next_city, path[next_city]))

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

bus = [[] for _ in range(N + 1)]
for _ in range(M):
    start, end, cost = map(int, sys.stdin.readline().split())
    bus[start].append((end, cost))

start_city, end_city = map(int, sys.stdin.readline().split())

# 최소 비용을 저장할 리스트
distance = [float('inf')] * (N + 1)
path = [[] for _ in range(N + 1)]

dijkstra(start_city)

print(distance[end_city])    # 최소 비용 출력
print(len(path[end_city]))    # 경로의 길이 출력
print(*path[end_city])    # 역순으로 출력하여 출발 도시부터 도착 도시까지의 경로 출력