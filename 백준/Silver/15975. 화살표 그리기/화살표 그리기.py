import sys
from collections import defaultdict

input = sys.stdin.readline

n = int(input().strip())
points = defaultdict(list)

for _ in range(n):
    x, c = map(int, input().strip().split())
    points[c].append(x)

total_distance = 0

for color in points:
    points[color].sort()
    if len(points[color]) > 1:
        for i in range(len(points[color])):
            if i == 0:
                total_distance += points[color][i + 1]- points[color][i]
            elif i == len(points[color]) - 1:
                total_distance += points[color][i]- points[color][i - 1]
            else:
                left_distance = points[color][i]- points[color][i - 1]
                right_distance = points[color][i + 1]- points[color][i]
                total_distance += min(left_distance, right_distance)

print(total_distance)