K = int(input())
for _ in range(K):
    P, M = map(int, input().split())

    seat = []
    fail = 0
    for _ in range(P):
        seatNo = int(input())
        if seatNo in seat:
            fail += 1
        else:
            seat.append(seatNo)

    print(fail)