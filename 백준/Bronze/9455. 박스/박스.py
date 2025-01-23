T = int(input())
for _ in range(T):
    m, n = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(m)]

    move_box = 0
    for j in range(n):
        cnt_empty = 0
        for i in range(m - 1, -1, -1):
            if boxes[i][j] == 1:
                move_box += cnt_empty
            else:
                cnt_empty += 1

    print(move_box)