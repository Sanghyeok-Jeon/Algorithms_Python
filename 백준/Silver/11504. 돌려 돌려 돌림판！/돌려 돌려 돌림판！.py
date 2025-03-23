T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    X = int(''.join(list(input().split())))
    Y = int(''.join(list(input().split())))
    data = ''.join(list(input().split()))

    data += data[:M -1]

    cnt = 0
    for i in range(len(data) - (M - 1)):
        Z = int(data[i:i + M])
        if X <= Z <= Y:
            cnt += 1

    print(cnt)