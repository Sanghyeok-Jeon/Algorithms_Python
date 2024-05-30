# 루트 노드를 찾는 함수
def find_root(parent, node):
    if parent[node] == node:
        return node

    parent[node] = find_root(parent, parent[node])

    return parent[node]

# 두 노드를 합치는 함수
def union(parent, rank, node1, node2):
    root1 = find_root(parent, node1)
    root2 = find_root(parent, node2)

    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1

n, m = map(int, input().split())    # 점의 개수, 선분의 개수
parent = [i for i in range(n)]    # 각 점의 부모 노드 초기화
rank = [0] * n    # 각 점의 랭크 초기화
cycle = False    # 사이클 여부

# 선분 정보 입력
for i in range(m):
    a, b = map(int, input().split())

    if find_root(parent, a) == find_root(parent, b):
        cycle = True
        print(i + 1)    # 사이클이 발생한 선분의 번호 출력
        break
    else:
        union(parent, rank, a, b)

# 사이클이 발생하지 않은 경우
if not cycle:
    print(0)