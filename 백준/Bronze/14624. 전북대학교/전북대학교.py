N = int(input())
if not N % 2:
    print('I LOVE CBNU')
else:
    print('*' * N)
    print(' ' * (N // 2) + '*')
    for i in range(1, N // 2 + 1):
        print(' ' * (N // 2 - i) + '*' + ' ' * (2 * i - 1) + '*')