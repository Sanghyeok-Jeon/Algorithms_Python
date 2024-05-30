N, M = map(int, input().split())
time_table = [input() for _ in range(N)]

possible_time = -1
for j in range(M):
    possible_yn = True
    for i in range(N):
        if time_table[i][j] == 'O':
            possible_yn = False
            break

    if possible_yn:
        possible_time = j + 1
        break

if possible_time >= 0:
    print(possible_time)
else:
    print('ESCAPE FAILED')