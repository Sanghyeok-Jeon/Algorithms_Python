K = int(input())
for k in range(K):
    h = int(input())
    data = input()

    for d in data:
        if h == 0:
            break

        if d == 'c':
            h += 1
        else:
            h -= 1

    print('Data Set {}:'.format(k+1))
    print(h)
    print()