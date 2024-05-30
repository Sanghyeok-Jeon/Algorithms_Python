data = list(map(int, input().split()))
order = input()

data.sort()

answer = []
for o in order:
    if o == 'A':
        answer.append(data[0])
    elif o == 'C':
        answer.append(data[2])
    else:
        answer.append(data[1])

print(*answer)