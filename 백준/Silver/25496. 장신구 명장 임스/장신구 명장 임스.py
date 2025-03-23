P, N = map(int, input().split())
A = sorted(list(map(int, input().split())))

cnt = 0
for a in A:
    if P < 200:
        cnt += 1
        P += a
    else:
        break

print(cnt)