def swapHorizontal(i, j):
    global max_candy

    cnt = 1
    for x in range(N-1):
        if candy[i][x] == candy[i][x+1]:
            cnt += 1
            max_candy = max(cnt, max_candy)
        else:
            cnt = 1

    cnt1 = 1
    cnt2 = 1
    for y in range(N-1):
        if candy[y][j] == candy[y+1][j]:
            cnt1 += 1
            max_candy = max(cnt1, max_candy)
        else:
            cnt1 = 1

        if candy[y][j+1] == candy[y+1][j+1]:
            cnt2 += 1
            max_candy = max(cnt2, max_candy)
        else:
            cnt2 = 1


def swapVertical(i, j):
    global max_candy

    cnt = 1
    for y in range(N-1):
        if candy[y][j] == candy[y+1][j]:
            cnt += 1
            max_candy = max(cnt, max_candy)
        else:
            cnt = 1

    cnt1 = 1
    cnt2 = 1
    for x in range(N-1):
        if candy[i][x] == candy[i][x+1]:
            cnt1 += 1
            max_candy = max(cnt1, max_candy)
        else:
            cnt1 = 1

        if candy[i+1][x] == candy[i+1][x+1]:
            cnt2 += 1
            max_candy = max(cnt2, max_candy)
        else:
            cnt2 = 1


N = int(input())
candy = [list(input()) for _ in range(N)]
max_candy = 0

for i in range(N):
    for j in range(N-1):
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]
        swapHorizontal(i, j)
        candy[i][j], candy[i][j+1] = candy[i][j+1], candy[i][j]

        cntH = 1
        if candy[i][j] == candy[i][j+1]:
            cntH += 1
            max_candy = max(max_candy, cntH)
        else:
            cntH = 1

for j in range(N):
    for i in range(N-1):
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]
        swapVertical(i, j)
        candy[i][j], candy[i+1][j] = candy[i+1][j], candy[i][j]

        cntV = 1
        if candy[i][j] == candy[i+1][j]:
            cntV += 1
            max_candy = max(max_candy, cntV)
        else:
            cntV = 1
        
print(max_candy)