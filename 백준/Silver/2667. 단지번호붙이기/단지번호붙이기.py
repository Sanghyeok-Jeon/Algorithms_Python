def DFS(i, j, count):
    data[i][j] = '0'

    di = [-1, 0, 1, 0]
    dj = [0, -1, 0, 1]

    for mode in range(4):
        next_i = i + di[mode]
        next_j = j + dj[mode]

        if (0 <= next_i < N) and (0 <= next_j < N) and (data[next_i][next_j] == '1'):
            count = DFS(next_i, next_j, count + 1)

    return count

N = int(input())
data = [list(str(input())) for _ in range(N)]
result = []

for i in range(N):
    for j in range(N):
        if data[i][j] == '1':
            result.append(DFS(i, j, 1))

for i in range(len(result)-1, 0, -1):
    for j in range(i):
        if result[j] > result[j+1]:
            result[j], result[j+1] = result[j+1], result[j]

print(len(result))
for i in range(len(result)):
    print(result[i])