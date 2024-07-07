T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    grill = [list(input()) for _ in range(H)]

    for i in range(H):
        for j in range(W - 1, -1, -1):
            print(grill[i][j], end='')
        print()