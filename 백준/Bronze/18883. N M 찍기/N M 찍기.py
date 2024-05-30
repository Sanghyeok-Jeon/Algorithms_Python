N, M = map(int, input().split())
for n in range(N):
    for m in range(1, M+1):
        if m != M:
            print(n*M + m, end=' ')
        else:
            print(n*M + m)