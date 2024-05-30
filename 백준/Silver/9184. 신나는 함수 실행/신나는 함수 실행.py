import sys

abc = [[[0] * 21 for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                abc[i][j][k] = 1
            else:
                if i < j < k:
                    abc[i][j][k] = abc[i][j][k-1] + abc[i][j-1][k-1] - abc[i][j-1][k]
                else:
                    abc[i][j][k] = abc[i-1][j][k] + abc[i-1][j-1][k] + abc[i-1][j][k-1] - abc[i-1][j-1][k-1]

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == b == c == -1:
        break

    originA, originB, originC = a, b, c

    if a <= 0 or b <= 0 or c <= 0:
        a = b = c = 0

    if a > 20 or b > 20 or c > 20:
        a = b = c = 20

    print(f'w({originA}, {originB}, {originC}) = {abc[a][b][c]}')