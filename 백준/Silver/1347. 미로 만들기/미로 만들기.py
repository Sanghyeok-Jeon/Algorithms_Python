N = int(input())
data = input()
maze = [[0]*101 for _ in range(101)]

start_i, start_j, end_i, end_j = 50, 50, 50, 50
now_i, now_j = start_i, start_j
maze[now_i][now_j] = 1

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]

mode = 0
for i in range(N):
    if data[i] == 'R':
        mode = (mode + 1) % 4
    elif data[i] == 'L':
        mode = (mode + 3) % 4
    else:
        now_i += di[mode]
        now_j += dj[mode]
        maze[now_i][now_j] = 1

        start_i = min(start_i, now_i)
        start_j = min(start_j, now_j)
        end_i = max(end_i, now_i)
        end_j = max(end_j, now_j)

for i in range(start_i, end_i+1):
    for j in range(start_j, end_j+1):
        if maze[i][j]:
            print('.', end='')
        else:
            print('#', end='')
    print()