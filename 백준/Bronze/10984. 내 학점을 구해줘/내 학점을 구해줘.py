T = int(input())
for _ in range(T):
    N = int(input())
    totalCredit = 0
    totalGrade = 0
    for _ in range(N):
        credit, grade = map(float, input().split())
        totalCredit += credit
        totalGrade += grade * credit

    print('{} {:.1f}'.format(int(totalCredit), totalGrade/totalCredit))