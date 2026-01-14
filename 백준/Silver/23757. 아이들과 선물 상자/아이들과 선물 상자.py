import heapq

def can_distribute_gifts(n, m, boxes, children):
    max_heap = [-box for box in boxes]
    heapq.heapify(max_heap)

    for child in children:
        largest_box = -heapq.heappop(max_heap)

        if largest_box < child:
            return False

        heapq.heappush(max_heap, -(largest_box - child))

    return True

n, m = map(int, input().split())
boxes = list(map(int, input().split()))
children = list(map(int, input().split()))

if can_distribute_gifts(n, m, boxes, children):
    print(1)
else:
    print(0)