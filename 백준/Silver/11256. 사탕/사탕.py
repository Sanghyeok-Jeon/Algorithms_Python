T = int(input())
for _ in range(T):
    J, N = map(int, input().split())

    box = []
    for _ in range(N):
        r, c = map(int, input().split())
        box.append(r * c)

    box.sort(reverse=True)

    cnt = 0
    for b in box:
        if J <= 0:
            break

        J -= b
        cnt += 1

    print(cnt)