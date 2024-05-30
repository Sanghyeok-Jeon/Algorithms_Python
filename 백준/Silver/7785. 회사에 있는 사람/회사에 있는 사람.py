n = int(input())

remindPerson = {}
for _ in range(n):
    person, io = input().split()
    if io == 'enter':
        remindPerson[person] = 'enter'
    else:
        del remindPerson[person]

for rp in sorted(remindPerson.keys(), reverse=True):
    print(rp)