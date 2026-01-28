import sys
from collections import deque
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())          # 주차공간 수, 차량 수
rate = [int(input()) for _ in range(n)]  # 자리별 단위요금
weight = [0]+ [int(input()) for _ in range(m)] # 차량별 무게(1-index)

events = [int(input()) for _ in range(2 * m)]   # +: 입차, -: 출차

# 비어있는 자리: 가장 작은 번호부터 배정해야 하므로 min-heap 사용
free_spots = list(range(n))  # 0..n-1
heapq.heapify(free_spots)

waiting = deque()            # 대기 차량
parked_spot = [None]* (m + 1)  # 차량 -> 주차 자리(0-index)

total = 0

for x in events:
    if x > 0:  # 입차
        car = x
        if free_spots:
            spot = heapq.heappop(free_spots)
            parked_spot[car]= spot
            total += rate[spot]* weight[car]
        else:
            waiting.append(car)
    else:      # 출차
        car = -x
        spot = parked_spot[car]
        parked_spot[car]= None

        heapq.heappush(free_spots, spot)

        # 대기 차량이 있으면 방금 빈 자리에 즉시 주차
        if waiting:
            next_car = waiting.popleft()
            spot2 = heapq.heappop(free_spots)
            parked_spot[next_car]= spot2
            total += rate[spot2]* weight[next_car]

print(total)