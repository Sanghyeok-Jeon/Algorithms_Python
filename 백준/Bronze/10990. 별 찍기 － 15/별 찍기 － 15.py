N = int(input())
for n in range(1, N+1):
    if n == 1:
        print(' '*(N-n) + '*')
    else:
        print(' '*(N-n) + '*' + ' '*(2*n-3) + '*')