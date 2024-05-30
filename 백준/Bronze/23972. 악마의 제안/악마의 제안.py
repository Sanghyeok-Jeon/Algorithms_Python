K, N = map(int, input().split())
if N == 1:
    print(-1)
else:
    cal = K * N // (N - 1) + 1 if (K * N) % (N - 1) else K * N // (N - 1)
    print(cal if cal >= 0 else -1)