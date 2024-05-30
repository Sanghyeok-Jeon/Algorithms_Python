N, M = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(N)]
numCandy = [[0]*(M+1) for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, M+1):
        numCandy[i][j] = maze[i-1][j-1] + max(numCandy[i-1][j-1], numCandy[i][j-1], numCandy[i-1][j])

print(numCandy[N][M])