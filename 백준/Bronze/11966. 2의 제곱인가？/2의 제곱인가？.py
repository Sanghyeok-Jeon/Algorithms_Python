N = int(input())

if N == 1:
    print(1)
else:
    while True:
        if N < 2:
            break

        if N % 2 == 0:
            N //= 2
        else:
            break

    if N == 1:
        print(1)
    else:
        print(0)