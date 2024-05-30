K = int(input())
origin_gist = ['G...', '.I.T', '..S.']
result = [[''] * (K * 4) for _ in range(K * 3)]

for i in range(K * 3):
    for j in range(K * 4):
        result[i][j] = origin_gist[i // K][j // K]

for i in range(K * 3):
    print(''.join(result[i]))