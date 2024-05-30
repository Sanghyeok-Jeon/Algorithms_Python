T = int(input())
data = list(map(int, input().split()))
score = [0, 0, 0, 0, 0]
for i in range(T):
    score[i] = data[i]

student_number = 0

if score[0] > score[2]:
    student_number += (score[0] - score[2]) * 508
else:
    student_number += (score[2] - score[0]) * 108

if score[1] > score[3]:
    student_number += (score[1] - score[3]) * 212
else:
    student_number += (score[3] - score[1]) * 305

if score[4]:
    student_number += score[4] * 707

print(student_number * 4763)