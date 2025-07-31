light = list(input())
light = ['N'] + light

cnt = 0
sw = 0
while True:
    if 'Y' not in light:
        print(cnt)
        break

    if sw > len(light):
        print(-1)
        break

    sw += 1
    if light[sw] == 'Y':
        cnt += 1
        for i in range(sw, len(light), sw):
            if light[i] == 'Y':
                light[i] = 'N'
            else:
                light[i] = 'Y'