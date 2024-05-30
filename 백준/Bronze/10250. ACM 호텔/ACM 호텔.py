T = int(input())
for tc in range(T):
    H, W, N = map(int, input().split())

    floor = N%H if N%H else H
    room = N//H + 1 if N%H else N//H

    print(floor*100 + room)