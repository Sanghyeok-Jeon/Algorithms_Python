import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

# 루트 노드를 찾는 함수
def find_root(parent, node):
    if parent[node] == node:
        return node
    parent[node] = find_root(parent, parent[node])

    return parent[node]


# 게이트를 도킹하는 함수
def dock_gate(parent, gate):
    root = find_root(parent, gate)
    if root == 0:  # 루트 노드가 0인 경우, 도킹할 수 없음
        return False
    parent[root] = root - 1  # 루트 노드의 부모를 갱신하여 도킹 처리

    return True

G = int(input())  # 게이트의 수
P = int(input())  # 비행기의 수
parent = [i for i in range(G + 1)] # 각 게이트의 부모 노드 초기화
count = 0  # 도킹된 비행기 수

# 비행기 도킹하기
for _ in range(P):
    gate = int(input())  # 도킹할 게이트 번호 : 1 ~ gate
    if not dock_gate(parent, gate):
        break
    count += 1

print(count)