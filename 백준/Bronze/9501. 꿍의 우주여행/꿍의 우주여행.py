T = int(input())
for _ in range(T):
    N, D = map(int, input().split())

    possible = 0
    for i in range(N):
        v, f, c = map(int, input().split())
        if v * f // c >= D:
            possible += 1

    print(possible)