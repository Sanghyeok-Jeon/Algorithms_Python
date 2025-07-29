n, m = map(int, input().split())

internal_nodes = n - m
u = 0
for i in range(n - 1):
    print(u, i + 1)

    if internal_nodes > u:
        u += 1