N = int(input())
map_ij = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            if map_ij[i][j] == 1 or (map_ij[i][k] == 1 and map_ij[k][j] == 1):
                map_ij[i][j] = 1

for i in map_ij:
    for j in i:
        print(j, end=' ')
    print()