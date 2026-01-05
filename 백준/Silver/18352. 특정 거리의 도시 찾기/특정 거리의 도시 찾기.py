from collections import deque
import sys

input = sys.stdin.readline

def find_cities_at_distance(n, m, k, x, roads):
    graph = [[]for _ in range(n + 1)]
    for a, b in roads:
        graph[a].append(b)

    distance = [-1] * (n + 1)
    distance[x] = 0

    queue = deque([x])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distance[neighbor] == -1:
                distance[neighbor] = distance[current] + 1
                queue.append(neighbor)

    result = [i for i in range(1, n + 1) if distance[i] == k]
    if result:
        for city in result:
            print(city)
    else:
        print(-1)

n, m, k, x = map(int, input().split())
roads = [tuple(map(int, input().split())) for _ in range(m)]

find_cities_at_distance(n, m, k, x, roads)