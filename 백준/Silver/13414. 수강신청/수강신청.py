import sys
from collections import OrderedDict

input = sys.stdin.readline

k, l = map(int, input().strip().split())
applications = OrderedDict()

for _ in range(l):
    student_id = input().strip()
    if student_id in applications:
        del applications[student_id]
    applications[student_id]= None

count = 0
for student_id in applications:
    if count == k:
        break
    print(student_id)
    count += 1