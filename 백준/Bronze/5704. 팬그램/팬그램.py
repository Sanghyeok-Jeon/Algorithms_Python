while True:
    S = input()

    alpha = [0] * 26

    if S == '*':
        break

    for s in S:
        if s.isalpha():
            alpha[ord(s) - ord('a')] = 1

    if sum(alpha) == 26:
        print('Y')
    else:
        print('N')