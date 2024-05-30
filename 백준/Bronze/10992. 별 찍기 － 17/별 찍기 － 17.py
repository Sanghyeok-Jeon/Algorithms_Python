N = int(input())
for n in range(N):
    if n == 0:
        print(' '*(N-n-1) + '*'*(n+1))
    else:
        if n == N-1:
            print('*'*(2*n+1))
        else:
            print(' '*(N-n-1) + '*' + ' '*(2*n-1) + '*')