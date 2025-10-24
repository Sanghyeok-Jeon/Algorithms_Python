T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())))

    cnt = 0
    m = 0
    for n in range(N):
        while m < M and A[n] > B[m]:
            m += 1

        cnt += m

    print(cnt)