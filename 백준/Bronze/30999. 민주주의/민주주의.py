N, M = map(int, input().split())
data = [list(input()) for _ in range(N)]

total = 0
for i in range(N):
    cnt = 0
    for j in range(M):
        if data[i][j] == 'O':
            cnt += 1

    if cnt > M // 2:
        total += 1

print(total)