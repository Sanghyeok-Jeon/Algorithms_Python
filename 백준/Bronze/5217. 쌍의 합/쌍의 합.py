n = int(input())
for _ in range(n):
    num = int(input())
    print('Pairs for {}: '.format(num), end='')
    for i in range(1, num//2 + 1):
        if i != num - i:
            if i == 1:
                print('{} {}'.format(i, num - i), end='')
            else:
                print(', {} {}'.format(i, num - i), end='')
    print()