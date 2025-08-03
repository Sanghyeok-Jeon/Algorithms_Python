N, T = map(int, input().split())

min_time = 2 ** 31
for _ in range(N):
    Si, Ii, Ci = map(int, input().split())

    cnt = 0
    while cnt < Ci:
        if Si >= T:
           min_time = min(min_time, Si - T)
           break

        cnt += 1
        Si += Ii

print(min_time if min_time != 2 ** 31 else -1)