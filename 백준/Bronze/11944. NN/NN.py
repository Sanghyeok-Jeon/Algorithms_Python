N, M = map(int, input().split())
NN = str(N) * N
if len(NN) > M:
    print(NN[:M])
else:
    print(NN)