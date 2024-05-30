def DFS(x, y):
    global end_x, end_y, feeling, possible

    if x == end_x and y == end_y:
        possible = 1

    for i in range(len(data)):
        if visited[i] == 0 and (abs(x-data[i][0]) + abs(y-data[i][1])) <= 1000:
            visited[i] = 1
            DFS(data[i][0], data[i][1])

T = int(input())

for tc in range(T):
    n = int(input())
    start_x, start_y = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(n+1)]
    end_x, end_y = data[-1][0], data[-1][1]
    visited = [0] * (n+1)
    feeling = 'sad'
    possible = 0

    DFS(start_x, start_y)

    if possible == 1:
        feeling = 'happy'

    print(feeling)