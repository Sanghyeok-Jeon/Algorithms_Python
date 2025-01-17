K = int(input())
data = input()

direction = 'right'
new_data = []
for i in range(0, len(data) - 1, K):
    if direction == 'right':
        new_data.append(data[i:i + K])
        direction = 'left'
    else:
        new_data.append(data[i:i + K][::-1])
        direction = 'right'

answer = ''
for j in range(K):
    for i in range(len(data) // K):
        answer += new_data[i][j]

print(answer)