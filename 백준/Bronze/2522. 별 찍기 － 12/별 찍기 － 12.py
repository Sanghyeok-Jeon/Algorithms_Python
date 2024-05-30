N = int(input())
for n in range(1, 2*N):
    print(' '*abs(N-n) + '*'*(N-abs(N-n)))