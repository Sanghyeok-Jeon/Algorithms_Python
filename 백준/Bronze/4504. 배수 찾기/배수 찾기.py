n = int(input())
while True:
    target = int(input())
    if not target:
        break

    if target % n:
        print('{} is NOT a multiple of {}.'.format(target, n))
    else:
        print('{} is a multiple of {}.'.format(target, n))