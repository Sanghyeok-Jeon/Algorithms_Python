n = int(input())
data = list(input().split())

student = {}
for i in range(n):
    student[data[i]] = 0

vote = []
for i in range(n):
    student_voted = list(input().split())
    for j in range(len(student_voted)):
        student[student_voted[j]] += 1

for i, v in sorted(student.items(), key=lambda x:(-x[1], x[0])):
    print(i, v)