n = int(input())
paintings = list(list(input() for _ in range(5)) for _ in range(n))

min_cnt_diff = 36
min_first = -1
min_second = -1
for i in range(n - 1):
    for j in range(i + 1, n):
        cnt_diff = 0
        for y in range(5):
            for x in range(7):
                if paintings[i][y][x] != paintings[j][y][x]:
                    cnt_diff += 1

        if cnt_diff < min_cnt_diff:
            min_cnt_diff = cnt_diff
            min_first = i
            min_second = j

print(min_first + 1, min_second + 1)