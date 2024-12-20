case = 1
while True:
    A = input()
    B = input()

    if A == B == 'END':
        break

    if sorted(A) == sorted(B):
        print('Case {}: {}'.format(case, 'same'))
    else:
        print('Case {}: {}'.format(case, 'different'))

    case += 1