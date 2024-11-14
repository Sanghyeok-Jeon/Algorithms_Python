N, C = map(int, input().split())

r, c = N, N
for _ in range(C):
    X, Y = map(int, input().split())

    if X >= r or Y >= c:
        continue

    if r * Y > X * c:
        c = Y
    else:
        r = X

print(r * c)