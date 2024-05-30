A, B = map(int, input().split())
K, X = map(int, input().split())

cnt = 0
for i in range(K - X, K + X + 1):
    if A <= i <= B:
        cnt += 1

if not cnt:
    print('IMPOSSIBLE')
else:
    print(cnt)