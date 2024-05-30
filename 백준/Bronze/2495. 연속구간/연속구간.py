for _ in range(3):
    num = input()

    maxSame = 0
    cntSame = 1
    n = num[0]
    for i in range(1, 8):
        if n == num[i]:
            cntSame += 1
        else:
            maxSame = max(maxSame, cntSame)
            n = num[i]
            cntSame = 1

    print(max(maxSame, cntSame))