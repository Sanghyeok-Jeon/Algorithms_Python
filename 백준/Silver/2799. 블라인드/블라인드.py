M, N = map(int, input().split())
windows = [input() for _ in range(5 * M + 1)]

answer = [0] * 5
for i in range(0, 5 * M, 5):
    for j in range(0, 5 * N, 5):
        cnt = 0
        for k in range(4):
            if windows[i + 1 + k][j + 1] == '*':
                cnt += 1

        answer[cnt] += 1

print(*answer)