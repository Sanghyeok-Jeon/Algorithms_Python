def rotate(i, d):
    if d == 1:
        gear[i] = gear[i][-1] + gear[i][:7]
    else:
        gear[i] = gear[i][1:8] + gear[i][0]

gear = [0] + [input() for _ in range(4)]
K = int(input())

for _ in range(K):
    gear_num, rotate_direction = map(int, input().split())
    direction = [0] * (4+1)
    direction[gear_num] = rotate_direction
    for i in range(gear_num, 4):
        if gear[i][2] != gear[i+1][6]:
            direction[i+1] = -direction[i]
    for i in range(gear_num, 1, -1):
        if gear[i][6] != gear[i-1][2]:
            direction[i-1] = -direction[i]
    for i in range(1, 5):
        if direction[i]:
            rotate(i, direction[i])

ans = 0
for i in range(1, 5):
    if gear[i][0] == '1':
        ans += (1 << (i-1))
print(ans)