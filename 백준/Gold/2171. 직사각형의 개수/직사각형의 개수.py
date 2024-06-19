from collections import defaultdict
from itertools import combinations
import sys
input = sys.stdin.readline

def count_rectangles(points):
    # x 좌표를 키로 하고, y 좌표 리스트를 값으로 하는 딕셔너리 생성
    x_dict = defaultdict(list)
    for x, y in points:
        x_dict[x].append(y)

    # y 좌표 쌍을 키로 하고, 그 쌍을 가진 x 좌표의 개수를 값으로 하는 딕셔너리 생성
    y_pairs = defaultdict(int)
    for x in x_dict:
        y_list = x_dict[x]
        y_list.sort()
        for y1, y2 in combinations(y_list, 2):
            y_pairs[(y1, y2)] += 1

    # 직사각형의 개수 계산
    rectangle_count = 0
    for (y1, y2), count in y_pairs.items():
        if count > 1:
            rectangle_count += count * (count - 1) // 2

    return rectangle_count

n = int(input())
points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

print(count_rectangles(points))