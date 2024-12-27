n, m = map(int, input().split())
bingo = list(input().split() for _ in range(n))

cnt_nine_row = []
for i in range(n):
    tmp_cnt_nine_row = 0
    for num in bingo[i]:
        tmp_cnt_nine_row += num.count('9')
    cnt_nine_row.append(tmp_cnt_nine_row)

cnt_nine_column = []
for i in range(m):
    tmp_cnt_nine_column = 0
    for j in range(n):
        tmp_cnt_nine_column += bingo[j][i].count('9')
    cnt_nine_column.append(tmp_cnt_nine_column)

print(sum(cnt_nine_row) - max(max(cnt_nine_row), max(cnt_nine_column)))