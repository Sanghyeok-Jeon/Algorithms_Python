N = int(input())
answer_students = input()
bsa = [0, 0, 0]
for a in answer_students:
    if a == 'B':
        bsa[0] += 1
    elif a == 'S':
        bsa[1] += 1
    else:
        bsa[2] += 1

max_cnt = max(bsa)
if max_cnt == bsa[0] == bsa[1] == bsa[2]:
    print('SCU')
else:
    if bsa[0] == max_cnt:
        print('B', end='')
    if bsa[1] == max_cnt:
        print('S', end='')
    if bsa[2] == max_cnt:
        print('A')
