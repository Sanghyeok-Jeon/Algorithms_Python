import heapq
import sys

# X번 학생으로부터 모든 학생까지의 최단 거리 계산
def dijkstra(start):
    distance = [float('inf')] * (N + 1)    # 시작점으로부터의 최단 거리를 저장할 리스트
    distance[start] = 0    # 시작점의 최단 거리는 0으로 초기화
    heap = []
    heapq.heappush(heap, (0, start))    # 우선순위 큐에 시작점과 최단 거리를 넣음

    while heap:
        dist, node = heapq.heappop(heap)    # 탐색 할 노드, 거리를 가져옴

        if distance[node] < dist:    # 기존에 있는 거리보다 길다면, 볼 필요도 없음
            continue

        for next_node, next_dist in graph[node]:
            cost = dist + next_dist    # 해당 노드를 거쳐 갈 때 거리

            if cost < distance[next_node]:    # 알고 있는 거리보다 작으면 갱신
                distance[next_node] = cost
                heapq.heappush(heap, (cost, next_node))    # 다음 인접 거리를 계산하기 위해 큐에 삽입

    return distance


N, M, X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]    # 각 노드의 연결된 도로 정보를 저장할 리스트

for _ in range(M):
    start, end, time = map(int, sys.stdin.readline().split())    # 도로의 시작점, 도로의 끝점, 왕복 시간
    graph[start].append((end, time))    # 시작점에서 끝점까지의 도로 정보 추가


# X번 마을에서부터 모든 학생까지의 최단 거리 계산
dist_from_X = dijkstra(X)

# 최대 거리
max_distance = 0

for i in range(1, N+1):
    if i == X:
        continue

    # 각 학생들로부터 X번 마을까지의 최단 거리 계산
    dist_to_X = dijkstra(i)
    total_distance = dist_from_X[i] + dist_to_X[X]    # X번 마을로부터 파티에 참석하는 학생 사이의 왕복 최단 거리

    if total_distance > max_distance:
        max_distance = total_distance

print(max_distance)

