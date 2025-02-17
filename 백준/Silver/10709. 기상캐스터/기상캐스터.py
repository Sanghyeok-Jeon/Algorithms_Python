H, W = map(int, input().split())
clouds = [input() for _ in range(H)]

cloud_time = [[0] * W for _ in range(H)]


for i in range(H):
    time = -1
    for j in range(W):
        if clouds[i][j] == 'c':
            time = 0

        cloud_time[i][j] = time
        if time != -1:
            time += 1

for i in range(H):
    print(*cloud_time[i])