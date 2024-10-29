T = int(input())
for _ in range(T):
    k = int(input())

    n = 0
    for i in range(k):
        n += 0.5
        n *= 2

    print(int(n))