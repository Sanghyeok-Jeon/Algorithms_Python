def multiply_matrix(matrix1, matrix2):
    result = [[0]*2 for _ in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += matrix1[i][k] * matrix2[k][j] % 1000000007

    return result

def power_matrix(matrix, n):
    if n == 1:
        return matrix
    else:
        tmp = power_matrix(matrix, n // 2)
        if n % 2 == 0:
            return multiply_matrix(tmp, tmp)
        else:
            return multiply_matrix(multiply_matrix(tmp, tmp), matrix)

def fibonacci(n):
    if n <= 1:
        return n

    matrix = [[1, 1], [1, 0]]
    result = power_matrix(matrix, n)
    return result[0][1]

n = int(input())
result = fibonacci(n)
print(result % 1000000007)