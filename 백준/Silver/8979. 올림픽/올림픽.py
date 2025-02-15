N, K = map(int, input().split())
medals = [list(map(int, input().split())) for _ in range(N)]

medals.sort(key=lambda x:(-x[1], -x[2], -x[3]))

idx = list(zip(*medals))[0].index(K)
for i in range(N):
    if medals[idx][1:] == medals[i][1:]:
        print(i + 1)
        break