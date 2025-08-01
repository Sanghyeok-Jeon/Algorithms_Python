import sys
import heapq

N = int(sys.stdin.readline())
heap = []
for i in range(N):
    x = int(sys.stdin.readline())
    if x:
        heapq.heappush(heap, (-x, x))
    else:
        if len(heap):
            print(heapq.heappop(heap)[1])
        else:
            print(0)