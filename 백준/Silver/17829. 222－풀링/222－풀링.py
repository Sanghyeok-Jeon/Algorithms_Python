def pooling(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]

    new_size = n // 2
    new_matrix = [[0] * new_size for _ in range(new_size)]

    for i in range(0, n, 2):
        for j in range(0, n, 2):
            block = [
                matrix[i][j], matrix[i][j+1],
                matrix[i+1][j], matrix[i+1][j+1]
            ]
            block.sort()
            new_matrix[i//2][j//2] = block[2]

    return pooling(new_matrix)

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = pooling(matrix)
print(result)