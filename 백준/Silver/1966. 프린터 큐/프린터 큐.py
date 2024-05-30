import collections

T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    q = collections.deque()
    order = list(map(int, input().split()))

    for i, v in enumerate(order):
        q.append((i, v))

    cntPrint = 0
    while len(q) > 0:
        if q[0][1] == max(order):
            cntPrint += 1
            if q[0][0] == M:
                print(cntPrint)
                break
            else:
                order.pop(0)
                q.popleft()
        else:
            order.append(order.pop(0))
            q.append(q.popleft())