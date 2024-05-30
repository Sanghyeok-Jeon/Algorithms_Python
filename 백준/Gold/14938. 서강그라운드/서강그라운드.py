import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, r = map(int, input().split())    # 지역의 개수, 수색범위, 길의 개수
items = [0] + list(map(int, input().split()))

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a][b] = l
    graph[b][a] = l

# 플로이드-워셜 알고리즘
for k in range(1, n + 1):    # 경유지
    for i in range(1, n + 1):    # 출발지
        for j in range(1, n + 1):    # 도착지
            if graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]

max_total_items = 0
for i in range(1, n + 1):    # 시작 지점
    temp_total_items = 0
    for j in range(1, n + 1):    # 도착 지점
        if i == j:    # 제자리인 경우
            graph[i][j] = 0

        if graph[i][j] <= m:    # 수색 범위 이내 지역인 경우
            temp_total_items += items[j]

    if temp_total_items > max_total_items:
        max_total_items = temp_total_items

print(max_total_items)