R, C = map(int, input().split())
I = [list(map(int, input().split())) for _ in range(R)]
T = int(input())

answer = 0
for i in range(0, R - 2):
    for j in range(0, C - 2):
        filtering = []
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                filtering.append(I[x][y])

        filtering.sort()

        if filtering[4] >= T:
            answer += 1

print(answer)