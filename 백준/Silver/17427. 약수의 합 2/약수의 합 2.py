import sys
n = int(sys.stdin.readline().strip())
ans = 0
for d in range(1, n + 1):
    ans += d * (n // d)
print(ans)
