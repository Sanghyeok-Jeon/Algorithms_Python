l = k = p = 0

for _ in range(3):
    S = input()
    if S[0] == 'l':
        l += 1
    elif S[0] == 'k':
        k += 1
    elif S[0] == 'p':
        p += 1

if l == k == p == 1:
    print('GLOBAL')
else:
    print('PONIX')