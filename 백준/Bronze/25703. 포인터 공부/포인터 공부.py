N = int(input())

print('int a;')
for i in range(1, N + 1):
    if i == 1:
        print('int *ptr = &a;')
    elif i == 2:
        print('int **ptr2 = &ptr;')
    else:
        print('int {}ptr{} = &ptr{};'.format('*' * i, i, i - 1))