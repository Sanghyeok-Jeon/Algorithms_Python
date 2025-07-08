N = int(input())
a = [input() for _ in range(N)]

x, y = 0, 0
for i in range(N):
    for j in range(N):
        if a[i][j] == '*':
            if a[i][j - 1] == '*' and a[i - 1][j] == '*':
                x, y = i, j

left_arm = 0
for j in range(y -1, -1, -1):
    if a[x][j] != '*':
        break
    else:
        left_arm += 1

right_arm = 0
for j in range(y + 1, N):
    if a[x][j] != '*':
        break
    else:
        right_arm += 1

waist = 0
waist_end = 0
for i in range(x + 1, N):
    if a[i][y] != '*':
        waist_end = i - 1
        break
    else:
        waist += 1

left_leg = 0
for i in range(waist_end + 1, N):
    if a[i][y - 1] != '*':
        break
    else:
        left_leg += 1

right_leg = 0
for i in range(waist_end + 1, N):
    if a[i][y + 1] != '*':
        break
    else:
        right_leg += 1

print(x + 1, y + 1)
print(left_arm, right_arm, waist, left_leg, right_leg)