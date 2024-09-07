case_number = 1
while True:
    n0 = int(input())
    if n0 == 0:
        break

    n1 = 3 * n0
    n1_type = ''
    if n1 % 2 == 1:
        n1_type = 'odd'
        n2 = (n1 + 1) // 2
    else:
        n1_type = 'even'
        n2 = n1 // 2

    n3 = 3 * n2
    n4 = n3 // 9

    print('{}. {} {}'.format(case_number, n1_type, n4))

    case_number += 1