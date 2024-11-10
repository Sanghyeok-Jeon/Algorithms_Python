while True:
    S = input()
    if S == '#':
        break

    quickSum = 0
    for i in range(len(S)):
        if S[i].isalpha():
            quickSum += (i + 1) * (ord(S[i]) - ord('A') + 1)

    print(quickSum)