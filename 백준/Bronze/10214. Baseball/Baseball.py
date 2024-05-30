T = int(input())
for _ in range(T):
    totalY, totalK = 0, 0
    for _ in range(9):
        Y, K = map(int, input().split())
        totalY += Y
        totalK += K

    print('Yonsei' if totalY > totalK else 'Korea' if totalY < totalK else 'Draw')