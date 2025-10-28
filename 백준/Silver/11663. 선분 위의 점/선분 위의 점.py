import bisect
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
points = list(map(int, input().split()))
points.sort()

for _ in range(M):
    a, b = map(int, input().split())
    left = bisect.bisect_left(points, a)
    right = bisect.bisect_right(points, b)
    print(right - left)