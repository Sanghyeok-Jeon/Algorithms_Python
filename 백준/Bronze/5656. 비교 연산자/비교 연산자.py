case = 1
while True:
    data = list(input().split())

    a = int(data[0])
    b = int(data[2])

    if data[1] == '>':
        print('Case {}: {}'.format(case, 'true' if a > b else 'false'))
    elif data[1] == '>=':
        print('Case {}: {}'.format(case, 'true' if a >= b else 'false'))
    elif data[1] == '<':
        print('Case {}: {}'.format(case, 'true' if a < b else 'false'))
    elif data[1] == '<=':
        print('Case {}: {}'.format(case, 'true' if a <= b else 'false'))
    elif data[1] == '==':
        print('Case {}: {}'.format(case, 'true' if a == b else 'false'))
    elif data[1] == '!=':
        print('Case {}: {}'.format(case, 'true' if a != b else 'false'))
    else:
        break

    case += 1