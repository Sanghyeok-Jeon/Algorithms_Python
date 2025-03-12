R, C = map(int, input().split())

master_data = [[i] for i in range(10)]
for i in range(R):
    line = input()[-2:0:-1]

    cnt_dot = 0
    for l in line:
        if l == '.':
            cnt_dot += 1
        else:
            master_data[int(l)].append(cnt_dot)
            break

tmp_data = sorted(master_data[1:], key=lambda x: x[1])

prev_dot_cnt = tmp_data[0][1]
rank = 1
for i in range(9):
    if tmp_data[i][1] == prev_dot_cnt:
        master_data[tmp_data[i][0]].append(rank)
    else:
        prev_dot_cnt = tmp_data[i][1]
        rank += 1
        master_data[tmp_data[i][0]].append(rank)

for i in range(1, 10):
    print(master_data[i][2])