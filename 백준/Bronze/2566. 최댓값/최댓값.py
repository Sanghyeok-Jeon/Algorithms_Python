data = [list(map(int, input().split())) for _ in range(9)]

r = c = 0
maxData = 0
for i in range(9):
    for j in range(9):
        if data[i][j] >= maxData:
            maxData = data[i][j]
            r, c = i+1, j+1

print(maxData)
print(r, c)