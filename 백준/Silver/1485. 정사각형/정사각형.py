def distance_squared(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

def is_square(points):
    distances = []
    for i in range(4):
        for j in range(i + 1, 4):
            distances.append(distance_squared(points[i], points[j]))

    distances.sort()

    return distances[0] == distances[1] == distances[2] == distances[3] and distances[4] == distances[5]

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    points = [tuple(map(int, input().split())) for _ in range(4)]
    if is_square(points):
        print(1)
    else:
        print(0)