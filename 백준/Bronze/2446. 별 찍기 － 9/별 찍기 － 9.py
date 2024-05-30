N = int(input())
for n in range(2*N+1):
    if n == N or n == N+1:
        continue
    print(' '*(N-abs(N-n)) + '*'*(2*abs(N-n)-1))