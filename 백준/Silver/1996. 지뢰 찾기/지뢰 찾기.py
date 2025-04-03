di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]

N = int(input())
map_mine = [input() for _ in range(N)]

map_cnt_mine = [[0] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if map_mine[i][j] != '.':
            cnt_mine = int(map_mine[i][j])
            for mode in range(8):
                ni = i + di[mode]
                nj = j + dj[mode]

                if 0 <= ni < N and 0 <= nj < N:
                    if map_mine[ni][nj] == '.':
                        map_cnt_mine[ni][nj] += cnt_mine

for i in range(N):
    for j in range(N):
        if map_mine[i][j] != '.':
            print('*', end='')
        elif map_cnt_mine[i][j] >= 10:
            print('M', end='')
        else:
            print(str(map_cnt_mine[i][j]), end='')
    print()