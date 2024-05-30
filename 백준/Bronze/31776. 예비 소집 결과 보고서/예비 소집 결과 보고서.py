N = int(input())
cnt = 0
for _ in range(N):
    t1, t2, t3 = map(int, input().split())

    if t1 == -1:
        continue

    if t1 != -1:
        if (t1 <= t2 <= t3) or (t1 <= t2 and t3 == -1) or (t2 == t3 == -1):
            cnt += 1
    elif t2 != -1:
        if (t1 <= t2 <= t3) or (t1 <= t2 and t3 == -1):
            cnt += 1
    elif t3 != -1:
        if t1 <= t2 <= t3:
            cnt += 1

print(cnt)