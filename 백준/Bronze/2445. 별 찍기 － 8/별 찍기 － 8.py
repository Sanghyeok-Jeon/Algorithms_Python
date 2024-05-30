N = int(input())
for n in range(1, 2*N+1):
    print('*'*(N-abs(N-n)) + ' '*abs(N-n)*2 + '*'*(N-abs(N-n)))