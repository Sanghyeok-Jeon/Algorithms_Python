N, L = map(int, input().split())
lights = [tuple(map(int, input().split())) for _ in range(N)]

position = 0
time = 0
for D, R, G in lights:
    time += (D - position)
    position = D

    cycle = time % (R + G)
    if cycle < R:
        time += (R - cycle)
        
time += (L - position)

print(time)
