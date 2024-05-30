import sys
input = sys.stdin.readline

def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])

    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

V, E = map(int, input().split())
parent = [i for i in range(V + 1)]

edges = []
for _ in range(E):
    A, B, C = map(int, input().split())
    edges.append((C, A, B))
edges.sort()    # 가중치 기준으로 오름차순 정렬

total_cost = 0
# 크루스칼 알고리즘
for i in range(E):
    cost, a, b = edges[i]
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total_cost += cost

print(total_cost)