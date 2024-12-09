case = 1
while True:
    L, P, V = map(int, input().split())

    if (L, P, V) == (0, 0, 0):
        break

    tmp = V % P if V % P <= L else L
    answer = V // P * L + tmp

    print('Case {}: {}'.format(case, answer))

    case += 1