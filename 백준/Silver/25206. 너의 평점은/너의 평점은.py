gradeDict = {'A+':4.5, 'A0':4.0, 'B+':3.5,
             'B0':3.0, 'C+':2.5, 'C0':2.0,
             'D+':1.5, 'D0':1.0, 'F':0.0}

totalPoint = 0
totalPointGrade = 0
for _ in range(20):
    subject, point, grade = input().split()
    if grade == 'P':
        continue
        
    totalPoint += float(point)
    totalPointGrade += float(point) * gradeDict[grade]

print(totalPointGrade / totalPoint)