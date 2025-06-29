N, M = map(int, input().split())
icecream = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    icecream[a][b] = True
    icecream[b][a] = True

result = 0
for i in range(1, N + 1):
    for j in range(i + 1, N + 1):
        if icecream[i][j]:
            continue

        for k in range(j + 1, N + 1):
            if not icecream[i][k] and not icecream[j][k]:
                result += 1

print(result)