data = list(map(int, input().split()))

answer = 'Good'
for i in range(1, len(data)):
    if data[i] < data[i - 1]:
        answer = 'Bad'
        break

print(answer)