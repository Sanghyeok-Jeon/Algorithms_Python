N = int(input())
paper = [[0] * 101 for _ in range(101)]

for num in range(1, N + 1):
    x, y, w, h = map(int, input().split())

    for i in range(x, x + w):
        for j in range(y, y + h):
            paper[i][j] = num

for num in range(1, N + 1):
    num_area = 0
    for p in paper:
        num_area += p.count(num)

    print(num_area)