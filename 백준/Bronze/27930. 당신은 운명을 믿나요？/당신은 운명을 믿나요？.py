S = input()

set_k = set()
set_y = set()
for i in range(len(S)):
    if S[i] in 'KOREA':
        set_k.add(S[i])
        if len(set_k) == 5:
            print('KOREA')
            exit()

    if S[i] in 'YONSEI':
        set_y.add(S[i])
        if len(set_y) == 6:
            print('YONSEI')
            exit()