N, K = map(int, input().split())

students = {
    '10':0, '11':0,
    '20':0, '21':0,
    '30':0, '31':0,
    '40':0, '41':0,
    '50':0, '51':0,
    '60':0, '61':0
}

for _ in range(N):
    S, Y = input().split()
    students[Y + S] += 1

rooms = 0
rooms += (students['10'] + students['11'] + students['20'] + students['21']) // K + 1 if (students['10'] + students['11'] + students['20'] + students['21']) % K else (students['10'] + students['11'] + students['20'] + students['21']) // K
rooms += (students['30'] + students['40']) // K + 1 if (students['30'] + students['40']) % K else (students['30'] + students['40']) // K
rooms += (students['31'] + students['41']) // K + 1 if (students['31'] + students['41']) % K else (students['31'] + students['41']) // K
rooms += (students['50'] + students['60']) // K + 1 if (students['50'] + students['60']) % K else (students['50'] + students['60']) // K
rooms += (students['51'] + students['61']) // K + 1 if (students['51'] + students['61']) % K else (students['51'] + students['61']) // K

print(rooms)