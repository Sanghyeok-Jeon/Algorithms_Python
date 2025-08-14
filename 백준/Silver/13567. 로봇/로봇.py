M, n = map(int, input().split())
data = [tuple(input().split()) for _ in range(n)]

di = [1, 0, -1, 0]
dj = [0, -1, 0, 1]
i, j = 0, 0
mode = 0
end_possible = True
for d in data:
    command, value = d

    if command == 'MOVE':
        ni = i + di[mode] * int(value)
        nj = j + dj[mode] * int(value)

        if 0 <= ni <= M and 0 <= nj <= M:
            i, j = ni, nj
        else:
            end_possible = False
            break

    else:
        if value == '0':
            mode = (mode - 1) % 4
        else:
            mode = (mode + 1) % 4

if end_possible:
    print(i, j)
else:
    print(-1)