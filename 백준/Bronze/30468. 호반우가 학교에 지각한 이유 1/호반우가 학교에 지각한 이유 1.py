s, d, i, l, N = map(int, input().split())
print(N * 4 - (s + d + i + l) if (s + d + i + l) // 4 < N else 0)