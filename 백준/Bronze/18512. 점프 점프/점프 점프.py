X, Y, P1, P2 = map(int, input().split())

while True:
    if P1 > P2:
        P2 += Y
    elif P1 < P2:
        P1 += X
    else:
        print(P1)
        break

    if P1 > 10000 or P2 > 10000:
        print(-1)
        break
