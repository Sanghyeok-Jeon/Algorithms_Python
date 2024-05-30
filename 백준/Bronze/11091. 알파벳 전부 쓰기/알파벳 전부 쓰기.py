N = int(input())
for _ in range(N):
    data = input().lower()
    alpha = [0] * 26

    for d in data:
        if d.isalpha():
            alpha[ord(d)-ord('a')] += 1

    if 0 in alpha:
        print('missing', end=' ')
        for i, v in enumerate(alpha):
            if not v:
                print(chr(ord('a') + i), end='')
        print()
    else:
        print('pangram')