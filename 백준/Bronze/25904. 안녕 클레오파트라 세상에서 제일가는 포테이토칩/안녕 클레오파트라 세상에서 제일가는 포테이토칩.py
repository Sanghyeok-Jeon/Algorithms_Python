N, X = map(int, input().split())
T = list(map(int, input().split()))

i = 0
while True:
    t = T[i % N]
    if t < X:
        print(i % N + 1)
        break

    X += 1
    i += 1