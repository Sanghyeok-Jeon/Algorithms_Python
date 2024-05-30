N = int(input())
tile = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        tile[i] = 1
    elif i == 2:
        tile[i] = 2
    else:
        tile[i] = ((tile[i-1] % 15746) + (tile[i-2] % 15746)) % 15746

print(tile[N])