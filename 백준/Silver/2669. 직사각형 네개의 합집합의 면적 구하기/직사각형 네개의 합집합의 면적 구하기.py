plane = [[0]*101 for _ in range(101)]

answer = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1+1, y2+1):
        for j in range(x1+1, x2+1):
            if not plane[i][j]:
                plane[i][j] = 1
                answer += 1

print(answer)