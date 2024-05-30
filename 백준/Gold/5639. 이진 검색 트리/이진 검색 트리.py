import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def post_order(start, end):
    if start > end:
        return

    mid = end + 1
    for i in range(start + 1, end + 1):
        if pre_order[i] > pre_order[start]:
            mid = i
            break

    post_order(start + 1, mid - 1) # 왼쪽 서브트리
    post_order(mid, end) # 오른쪽 서브트리
    print(pre_order[start]) # 루트 노드

pre_order = []
while True:
    try:
        pre_order.append(int(input()))
    except:
        break

post_order(0, len(pre_order) - 1)