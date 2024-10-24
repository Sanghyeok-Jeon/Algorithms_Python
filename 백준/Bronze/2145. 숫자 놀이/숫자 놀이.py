while True:
    N = int(input())

    if N == 0:
        break

    while N >= 10:
        N = sum(map(int, str(N)))

    print(N)