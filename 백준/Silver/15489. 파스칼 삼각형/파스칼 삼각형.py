R, C, W = map(int, input().split())

pascal = [[0]*30 for _ in range(30)]
for i in range(1, 30):
    for j in range(1, i+1):
        if i == 1 and j == 1:
            pascal[i][j] = 1
        else:
            pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]

answer = 0
for i in range(W):
    for j in range(i+1):
        answer += pascal[R+i][C+j]

print(answer)