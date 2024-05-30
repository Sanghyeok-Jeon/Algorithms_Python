import sys
import heapq

def sync(Q):
    while Q and not visited[Q[0][1]]:
        heapq.heappop(Q)

T = int(sys.stdin.readline())
for _ in range(T):
    k = int(sys.stdin.readline())
    maxQ = []
    minQ = []
    visited = [0] * 1000001
    for i in range(k):
        order, num = sys.stdin.readline().rstrip().split()
        num = int(num)

        if order == 'I':
            heapq.heappush(maxQ, (-num, i))
            heapq.heappush(minQ, (num, i))
            visited[i] = 1
        else:
            if num == 1:
                sync(maxQ)
                if maxQ:
                    visited[maxQ[0][1]] = 0
                    heapq.heappop(maxQ)
            else:
                sync(minQ)
                if minQ:
                    visited[minQ[0][1]] = 0
                    heapq.heappop(minQ)

    sync(maxQ)
    sync(minQ)

    if len(maxQ):
        print(-maxQ[0][0], minQ[0][0])
    else:
        print('EMPTY')