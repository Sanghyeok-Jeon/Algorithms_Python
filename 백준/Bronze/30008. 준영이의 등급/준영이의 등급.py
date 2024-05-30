def check_degree(N, g):
    pct_g = g * 100 // N

    result = 0
    if pct_g <= 4:
        result = 1
    elif pct_g <= 11:
        result = 2
    elif pct_g <= 23:
        result = 3
    elif pct_g <= 40:
        result = 4
    elif pct_g <= 60:
        result = 5
    elif pct_g <= 77:
        result = 6
    elif pct_g <= 89:
        result = 7
    elif pct_g <= 96:
        result = 8
    else:
        result = 9

    return result

N, K = map(int, input().split())
G = list(map(int, input().split()))

D = [0] * K
for i in range(K):
    D[i] = check_degree(N, G[i])

print(*D)