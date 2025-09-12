def is_inside_planet(x, y, cx, cy, r):
    return (x - cx) ** 2 + (y - cy) ** 2 <= r ** 2

def count_passes(start, end, planets):
    passes = 0

    for cx, cy, r in planets:
        start_indide = is_inside_planet(start[0], start[1], cx, cy, r)
        end_indide = is_inside_planet(end[0], end[1], cx, cy, r)

        if start_indide != end_indide:
            passes += 1

    return passes

T = int(input())
for _ in range(T):
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    planets = [list(map(int, input().split())) for _ in range(n)]

    start = (x1, y1)
    end = (x2, y2)

    print(count_passes(start, end, planets))