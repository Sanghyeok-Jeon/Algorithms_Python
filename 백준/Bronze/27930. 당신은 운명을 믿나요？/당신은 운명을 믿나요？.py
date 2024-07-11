S = input()

K = 'KOREA'
Y = 'YONSEI'
idx_k, idx_y = 0, 0
for i in range(len(S)):
    if idx_k == len(K):
        print('KOREA')
        break

    if idx_y == len(Y):
        print('YONSEI')
        break

    if S[i] == K[idx_k]:
        idx_k += 1

    if S[i] == Y[idx_y]:
        idx_y += 1