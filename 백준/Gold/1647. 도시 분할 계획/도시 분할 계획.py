import sys
input = sys.stdin.readline

# Union-Find 알고리즘을 위한 함수
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])

    return parent[x]

def union_parent(parent, root_a, root_b):
    if root_a < root_b:
        parent[root_b] = root_a
    else:
        parent[root_a] = root_b

N, M = map(int, input().split())
edges = []    # 간선 정보를 저장할 리스트
for _ in range(M):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))    # 비용, 출발점, 도착점 순으로 저장

# 비용을 기준으로 간선을 오름차순으로 정렬
edges.sort()

# Union-Find 알고리즘을 위한 부모 테이블 초기화
parent = [i for i in range(N + 1)]

# 최소 신장 트리 구하기
total_cost = 0    # 최소 신장 트리의 비용을 저장할 변수
max_cost = 0    # 가장 비용이 큰 간선의 비용을 저장할 변수
for edge in edges:
    cost, a, b = edge
    root_a = find_parent(parent, a)
    root_b = find_parent(parent, b)
    if root_a != root_b:    # 사이클이 형성되지 않으면
        union_parent(parent, root_a, root_b)    # 두 집합을 합침
        total_cost += cost    # 비용을 더함
        if max_cost < cost:    # 가장 비용이 큰 간선의 비용 갱신
            max_cost = cost
            
# 가장 비용이 큰 간선의 비용을 최소 신장 트리의 비용에서 뺀 결과 출력
print(total_cost - max_cost)