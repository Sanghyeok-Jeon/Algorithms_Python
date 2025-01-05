while True:
    data = list(map(int, input().split()))

    if data == [-1]:
        break

    cnt = 0
    for d in data:
        if d * 2 in data and d != 0:
            cnt += 1

    print(cnt)