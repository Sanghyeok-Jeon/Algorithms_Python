puzzle_answer = ['ABCD', 'EFGH', 'IJKL', 'MNO.']
puzzle_scattered = list(input() for _ in range(4))

alpha_scattered = dict()
for i in range(4):
    for j in range(4):
        if puzzle_answer[i][j] != puzzle_scattered[i][j] and puzzle_scattered[i][j] != '.':
            alpha_scattered[puzzle_scattered[i][j]] = (i, j)

total_mahattan_distance = 0
for i in range(4):
    for j in range(4):
        if puzzle_answer[i][j] in alpha_scattered.keys():
            mahattan_distance = abs(alpha_scattered[puzzle_answer[i][j]][0] - i) + abs(alpha_scattered[puzzle_answer[i][j]][1] - j)
            total_mahattan_distance += mahattan_distance

print(total_mahattan_distance)