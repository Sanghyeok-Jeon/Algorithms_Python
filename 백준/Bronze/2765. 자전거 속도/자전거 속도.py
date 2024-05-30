trip = 1
while True:
    l, r, t = map(float, input().split())
    if r == 0:
        break

    D = (l * 3.141592) * r / 63360
    V = D/t*3600
    print('Trip #{}: {:.2f} {:.2f}'.format(trip, D, V))

    trip += 1