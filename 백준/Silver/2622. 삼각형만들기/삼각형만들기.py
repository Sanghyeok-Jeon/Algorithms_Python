N = int(input())

cnt = 0
for a in range(1, N // 3 + 1):
    for b in range(a, (N - a) // 2 + 1):
        c = N - (a + b)
        if c < b:
            break
        if a + b > c:
            cnt += 1

print(cnt)