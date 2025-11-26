def restore_array(H, W, X, Y, B):
    A = [[0]* W for _ in range(H)]

    for i in range(H):
        for j in range(W):
            A[i][j] = B[i][j]
            if i >= X and j >= Y:
                A[i][j] -= A[i - X][j - Y]

    return A

import sys
input = sys.stdin.readline

H, W, X, Y = map(int, input().strip().split())
B = [list(map(int, input().strip().split())) for _ in range(H + X)]

A = restore_array(H, W, X, Y, B)

for row in A:
    print(' '.join(map(str, row)))