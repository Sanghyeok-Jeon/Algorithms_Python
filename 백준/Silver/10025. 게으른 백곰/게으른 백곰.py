import sys

input = sys.stdin.readline

N, K = map(int, input().split())
buckets = [0] * 1000001

for _ in range(N):
    g, x = map(int, input().split())
    buckets[x] += g

window = 2 * K + 1
max_ice = 0

current = sum(buckets[:window])
max_ice = current

for i in range(window, 1000001):
    current += buckets[i] - buckets[i - window]
    if current > max_ice:
        max_ice = current

print(max_ice)