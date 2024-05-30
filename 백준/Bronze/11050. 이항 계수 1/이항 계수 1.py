N, K = map(int, input().split())
bunmo, bunja = 1, 1

for i in range(max(N-K, K)+1, N+1):
    bunmo *= i

for i in range(1, min(N-K, K)+1):
    bunja *= i

print(bunmo//bunja)