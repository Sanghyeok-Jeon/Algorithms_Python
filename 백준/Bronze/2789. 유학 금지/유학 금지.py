data = input()
targetDelete = 'CAMBRIDGE'

answer = ''
for d in data:
    if d not in targetDelete:
        answer += d

print(answer)