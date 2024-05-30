import sys

def bellman_ford(graph, N, start):
    distance = [INF] * (N + 1)    # 각 노드까지의 최단 거리를 저장
    distance[start] = 0

    # N-1번 반복하여 최단 거리 갱신
    for _ in range(N - 1):
        for u in range(1, N + 1):
            for v, w in graph[u]:    # u 노드와 연결되 모든 간선에 대해 반복. v: 도착 노드, w: 가중치.
                if distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w

    # 음수 사이클 검사
    for u in range(1, N + 1):
        for v, w in graph[u]:
            if distance[u] + w < distance[v]:
                return 'YES'    # 음수 사이클이 존재하는 경우

    return 'NO'    # 음수 사이클이 존재하지 않는 경우

INF = int(2e9)

TC = int(sys.stdin.readline())
for _ in range(TC):
    N, M, W = map(int, sys.stdin.readline().split())    # 노드 수, 도로 수, 웜홀 수
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        S, E, T = map(int, sys.stdin.readline().split())    # 출발 노드, 도착 노드, 소요 시간

        graph[S].append((E, T))    # 양방향이므로 양쪽 노드에 추가
        graph[E].append((S, T))

    for _ in range(W):
        S, E, T = map(int, sys.stdin.readline().split())

        graph[S].append((E, -T))    # 웜홀은 시간이 거꾸로 흐르니까 음수로 추가

    result = bellman_ford(graph, N, 1)    # 벨만-포드 알고리즘 수행

    print(result)