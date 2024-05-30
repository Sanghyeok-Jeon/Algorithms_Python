import math

# 두 점 사이의 거리를 계산하는 함수
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# 루트 노드를 찾는 함수
def find_root(parent, node):
    if parent[node] != node:
        parent[node] = find_root(parent, parent[node])

    return parent[node]

# 두 노드를 합치는 함수
def union(parent, rank, node1, node2):
    root1 = find_root(parent, node1)
    root2 = find_root(parent, node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

# 크루스칼 알고리즘을 사용하여 최소 신장 트리의 가중치 합을 구하는 함수
def kruskal(edges, n):
    # 각 노드의 부모 노드를 저장하는 리스트
    parent = [i for i in range(n + 1)]

    rank = [0] * (n + 1)    # 각 노드의 랭크를 저장
    result = 0    # 최소 신장 트리의 가중치 합을 저장

    for edge in edges:
        cost, node1, node2 = edge
        if find_root(parent, node1) != find_root(parent, node2):
            union(parent, rank, node1, node2)
            result += cost

    return result

n = int(input())    # 별의 개수
stars = [tuple(map(float, input().split())) for _ in range(n)]    # 별의 좌표

# 각 별 사이의 거리와 노드를 저장하는 리스트
edges = []
for i in range(n - 1):
    for j in range(i + 1, n):
        x1, y1 = stars[i]
        x2, y2 = stars[j]
        distance = calculate_distance(x1, y1, x2, y2)
        edges.append((distance, i, j))

# 거리를 기준으로 오름차순 정렬
edges.sort()

# 최소 신장 트리의 가중치 합 구하기
result = kruskal(edges, n)

print(round(result, 2))