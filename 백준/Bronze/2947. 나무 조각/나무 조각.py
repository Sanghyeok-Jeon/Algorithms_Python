wood = list(map(int, input().split()))

while True:
    if wood == [1, 2, 3, 4, 5]:
        break

    if wood[0] > wood[1]:
        wood[0], wood[1] = wood[1], wood[0]
        print(*wood)

    if wood[1] > wood[2]:
        wood[1], wood[2] = wood[2], wood[1]
        print(*wood)

    if wood[2] > wood[3]:
        wood[2], wood[3] = wood[3], wood[2]
        print(*wood)

    if wood[3] > wood[4]:
        wood[3], wood[4] = wood[4], wood[3]
        print(*wood)
