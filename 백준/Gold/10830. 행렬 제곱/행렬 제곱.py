import sys
input = sys.stdin.readline

# 행렬 x 행렬
def multiple(n, m1, m2):
    result = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += m1[i][k] * m2[k][j]
            result[i][j] %= 1000

    return result

# 분할 정복을 이용한 거듭제곱
def power(n, b, m):
    if b == 1:
        return m
    elif b == 2:
        return multiple(n, m, m)
    else:
        half = power(n, b // 2, m)

        if b % 2:
            return multiple(n, multiple(n, half, half), m)
        else:
            return multiple(n, half, half)

N, B = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(N)]

answer = power(N, B, matrix)

for ans in answer:
    for a in ans:
        print(a % 1000, end=' ')
    print()