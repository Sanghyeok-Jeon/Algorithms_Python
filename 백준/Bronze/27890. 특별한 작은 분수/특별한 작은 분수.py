x, N = map(int, input().split())
for i in range(N):
    x = (x//2) ^ 6 if not x % 2 else (2*x) ^ 6
print(x)