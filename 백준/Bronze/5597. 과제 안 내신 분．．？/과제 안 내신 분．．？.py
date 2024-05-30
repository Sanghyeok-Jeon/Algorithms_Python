student = [1] * 30
for _ in range(28):
    n = int(input()) - 1
    student[n] -= 1

for i in range(len(student)):
    if student[i]:
        print(i+1)