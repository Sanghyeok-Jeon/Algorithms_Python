def min_arrow_length(n, points):
    color_points = {}

    for point, color in points:
        if color not in color_points:
            color_points[color] = []

        color_points[color].append(point)

    total_length = 0

    for color in color_points:
        color_points[color].sort()
        points_list = color_points[color]

        for i in range(len(points_list)):
            if i == 0:
                total_length += points_list[i + 1] - points_list[i]
            elif i == len(points_list) - 1:
                total_length += points_list[i] - points_list[i - 1]
            else:
                total_length += min(points_list[i] - points_list[i - 1], points_list[i + 1] - points_list[i])

    return total_length

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

print(min_arrow_length(n, points))