D, K = map(int, input().split())

dpA = [0] * 31
dpB = [0] * 31

dpA[1] = 1
dpB[2] = 1
for i in range(3, 31):
    dpA[i] = dpA[i-1] + dpA[i-2]
    dpB[i] = dpB[i-1] + dpB[i-2]

for i in range(1, 1000001):
    if not (K - dpA[D]*i) % dpB[D]:
        print(i)
        print((K - dpA[D]*i)//dpB[D])
        break