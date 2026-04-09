import sys
from collections import deque

input = sys.stdin.readline

n, w, L = map(int, input().split())
trucks = deque(map(int, input().split()))

bridge = deque([0] * w)
bridge_weight = 0
time = 0

while trucks:
    time += 1

    bridge_weight -= bridge.popleft()

    if bridge_weight + trucks[0] <= L:
        truck = trucks.popleft()
        bridge.append(truck)
        bridge_weight += truck
    else:
        bridge.append(0)

time += w

print(time)