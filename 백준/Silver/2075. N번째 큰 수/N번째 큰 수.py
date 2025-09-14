import heapq
import sys

input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    nums = list(map(int, input().split()))

    for num in nums:
        if len(heap) < N:
            heapq.heappush(heap, num)
        else:
            if heap[0] < num:
                heapq.heappush(heap, num)
                heapq.heappop(heap)

print(heap[0])