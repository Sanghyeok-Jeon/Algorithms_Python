K = int(input())
C = int(input())
for i in range(C):
    M, N = map(int, input().split())

    if M < N:
        if N - M - 1 >= K - N + 1:
            print(0)
        else:
            print(1)
    elif M > N:
        if M - N - 1 > K - M + 1:
            print(0)
        else:
            print(1)
    else:
        print(1)