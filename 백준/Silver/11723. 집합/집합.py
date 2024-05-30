import sys

M = int(sys.stdin.readline())
S = [0] * 21

for _ in range(M):
    x = 0
    c = sys.stdin.readline().split()
    if len(c) > 1:
        x = int(c[1])

    if c[0] == 'add':
        S[x] = 1
    elif c[0] == 'remove':
        if S[x] == 1:
            S[x] = 0
    elif c[0] == 'check':
        if S[x] == 0:
            print(0)
        else:
            print(1)
    elif c[0] == 'toggle':
        if S[x] == 0:
            S[x] = 1
        else:
            S[x] = 0
    elif c[0] == 'all':
        S = [1] * 21
    else:
        S = [0] * 21