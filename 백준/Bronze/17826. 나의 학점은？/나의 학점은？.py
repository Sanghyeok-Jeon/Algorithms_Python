scores = list(map(int, input().split()))
target = int(input())

if scores.index(target) < 5:
    print('A+')
elif scores.index(target) < 15:
    print('A0')
elif scores.index(target) < 30:
    print('B+')
elif scores.index(target) < 35:
    print('B0')
elif scores.index(target) < 45:
    print('C+')
elif scores.index(target) < 48:
    print('C0')
else:
    print('F')