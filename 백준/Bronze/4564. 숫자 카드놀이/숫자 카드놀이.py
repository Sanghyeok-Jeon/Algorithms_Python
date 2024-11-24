while True:
    S = input()

    if S == '0':
        break

    while len(S) > 1:
        print(S, end=' ')

        tmp = 1
        for s in S:
            tmp *= int(s)

        S = str(tmp)

    print(S)

