n, T = map(int, input().split())
process = list(map(int, input().split()))

cnt = 0
for p in process:
    if T - p >= 0:
        cnt += 1
        T -= p
    else:
        break

print(cnt)