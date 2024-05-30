def cost():
    result = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j]:
                result += flowers[i][j]
    return result

def cancel(i, j):
    for mode in range(5):
        ni = i + di[mode]
        nj = j + dj[mode]
        visited[ni][nj] = 0

def select(i, j):
    for mode in range(5):
        ni = i + di[mode]
        nj = j + dj[mode]
        visited[ni][nj] = 1

def checkImpossible(i, j):
    for mode in range(5):
        ni = i + di[mode]
        nj = j + dj[mode]
        if visited[ni][nj]:
            return 0
    return 1

def DFS(cnt):
    global min_cost

    if cnt == 3:
        min_cost = min(min_cost, cost())
        return

    for m in range(1, N-1):
        for n in range(1, N-1):
            if checkImpossible(m, n):
                select(m, n)
                DFS(cnt+1)
                cancel(m, n)

N = int(input())
flowers = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*N for _ in range(N)]
min_cost = 201 * 5 * 3
di = [1, -1, 0, 0, 0]
dj = [0, 0, 1, -1, 0]

DFS(0)

print(min_cost)