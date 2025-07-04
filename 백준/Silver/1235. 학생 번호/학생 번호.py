N = int(input())
origin_student_no = [input() for _ in range(N)]

len_student_no = len(origin_student_no[0])

for n in range(1, len_student_no + 1):
    tmp_student_no = set()
    for i in range(N):
        tmp_student_no.add(origin_student_no[i][-n:])

    if len(origin_student_no) == len(tmp_student_no):
        print(n)
        break