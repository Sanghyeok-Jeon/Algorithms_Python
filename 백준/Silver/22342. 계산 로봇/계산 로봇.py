import sys
input = sys.stdin.readline

M, N = map(int, input().split())

value_input = [list(map(int, input().rstrip())) for _ in range(M)]
value_save = [[0] * (N + 2) for _ in range(M + 2)]
value_output = [[0] * (N + 2) for _ in range(M + 2)]

for i in range(1, M + 1):
    value_output[i][1] = value_input[i - 1][0]

result = 0
for j in range(2, N + 1):
    for i in range(1, M + 1):
        value_save[i][j] = max(value_output[i -1][j - 1], value_output[i][j - 1], value_output[i + 1][j - 1])

        value_output[i][j] = value_save[i][j] + value_input[i - 1][j - 1]

        result = max(result, value_save[i][j])

print(result)