def Upsampling(i, j):
    for x in range(i*K, i*K+K):
        for y in range(j*K, j*K+K):
            imgUpsampling[x][y] = imgOrigin[i][j]

N, K = map(int, input().split())
imgOrigin = [list(map(int, input().split())) for _ in range(N)]
imgUpsampling = [[0]*N*K for _ in range(N*K)]

for i in range(N):
    for j in range(N):
        Upsampling(i, j)

for i in range(N*K):
    print(*imgUpsampling[i])