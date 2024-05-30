data = input()

cnt = 0
i = 0
while i < len(data) - 3:
    if data[i] == 'D':
        if data[i:i+4] == 'DKSH':
            cnt += 1
            i += 4
            continue
    i += 1

print(cnt)