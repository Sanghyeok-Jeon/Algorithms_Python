N = int(input())

print('*' * N + ' ' * (2 * (N - 1) - 1) + '*' * N)

for i in range(1, N - 1):
    print(' ' * i, end='')
    print('*' + ' ' * (N - 2) + '*', end='')
    print(' ' * (2 * (N - 1 - i) - 1), end='')
    print('*' + ' ' * (N - 2) + '*')

print(' ' * (N - 1), end='')
print('*' + ' ' * (N - 2) + '*', end='')
print(' ' * (N - 2) + '*')

for i in range(N - 2, 0, -1):
    print(' ' * i, end='')
    print('*' + ' ' * (N - 2) + '*', end='')
    print(' ' * (2 * (N - 1 - i) - 1), end='')
    print('*' + ' ' * (N - 2) + '*')

print('*' * N + ' ' * (2 * (N - 1) - 1) + '*' * N)