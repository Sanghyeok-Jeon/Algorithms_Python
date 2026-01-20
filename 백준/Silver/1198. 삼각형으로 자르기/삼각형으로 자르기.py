def calculate_area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

def max_triangle_area(points):
    max_area = 0
    n = len(points)

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                x3, y3 = points[k]
                area = calculate_area(x1, y1, x2, y2, x3, y3)
                max_area = max(max_area, area)

    return max_area

n = int(input().strip())
points = [tuple(map(int, input().strip().split())) for _ in range(n)]

print(max_triangle_area(points))