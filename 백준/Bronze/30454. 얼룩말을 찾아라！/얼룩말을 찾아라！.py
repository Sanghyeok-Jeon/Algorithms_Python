N, L = map(int, input().split())
zebra = [input() for _ in range(N)]
line_cnt = [0] * N

for i in range(N):
    now_hair = zebra[i][0]
    cnt_hair = 0 if now_hair == '0' else 1
    for j in range(1, L):
        if now_hair == '0':
            if zebra[i][j] == '0':
                continue
            else:
                cnt_hair += 1
                now_hair = zebra[i][j]
        else:
            if zebra[i][j] == '0':
                now_hair = zebra[i][j]
            else:
                continue

    line_cnt[i] = cnt_hair

max_line = max(line_cnt)
print(max_line, line_cnt.count(max_line))