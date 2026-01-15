import sys

def precompute_visible_points(max_n):
    phi = list(range(max_n + 1))
    visible_points = [0] * (max_n + 1)

    for i in range(2, max_n + 1):
        if phi[i]== i:
            for j in range(i, max_n + 1, i):
                phi[j] *= (i - 1)
                phi[j] //= i

    for i in range(1, max_n + 1):
        visible_points[i] = visible_points[i - 1] + phi[i]

    return visible_points

max_n = 1000
visible_points = precompute_visible_points(max_n)

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    print(visible_points[n]* 2 + 1)