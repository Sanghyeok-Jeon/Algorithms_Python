N, M = map(int, input().split())
floor = [input() for _ in range(N)]

cnt = 0

for i in range(N):
    j = 0
    while j < M:
        if floor[i][j] == '|':
            j += 1
        else:
            cnt += 1
            while j < M and floor[i][j] == '-':
                j += 1

for j in range(M):
    i = 0
    while i < N:
        if floor[i][j] == '-':
            i += 1
        else:
            cnt += 1
            while i < N and floor[i][j] == '|':
                i += 1

print(cnt)