T = int(input())
for _ in range(T):
    N, M, k, D = map(int, input().split())

    B = 2 * D // (k * N * M * (M - 1) + M * M * N * (N - 1))

    if B:
        print(M * (M - 1) * N * k * B // 2 + M * M * N * (N - 1) * B // 2)
    else:
        print(-1)