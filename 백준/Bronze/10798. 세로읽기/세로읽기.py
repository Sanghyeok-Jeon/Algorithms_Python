answer = ['' for _ in range(15)]
for _ in range(5):
    tmpStr = list(input())
    for i in range(len(tmpStr)):
        answer[i] += tmpStr[i]

print(''.join(answer))