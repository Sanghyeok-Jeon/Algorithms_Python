data = input()

cnt = 1
for i in range(len(data)):
    if cnt < 10:
        print(data[i], end='')
        cnt += 1
    elif cnt == 10:
        print(data[i])
        cnt = 1