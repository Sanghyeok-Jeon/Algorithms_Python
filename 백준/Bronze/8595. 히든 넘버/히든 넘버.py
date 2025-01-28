n = int(input())
data = input()

answer = 0
hidden_start = -1
hidden_exist = False
for i in range(n):
    if hidden_start != -1:
        if data[i].isnumeric():
            continue
        else:
            answer += int(data[hidden_start:i])
            hidden_start = -1
    else:
        if data[i].isnumeric():
            hidden_start = i
            hidden_exist = True
        else:
            continue

if hidden_start != -1:
    answer += int(data[hidden_start:n])

if hidden_exist:
    print(answer)
else:
    print(0)