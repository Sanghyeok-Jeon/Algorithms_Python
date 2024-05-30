A, B, C, M = map(int, input().split())
piro = 0
work = 0

for i in range(24):
    if piro + A <= M:
        work += B
        piro += A
    else:
        piro -= C
        if piro < 0:
            piro = 0

print(work)