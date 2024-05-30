N = int(input())
if not N % 2:
    for i in range(1, N+1):
        print((N//2)*'* ')
        print(' *'*(N//2))
else:
    for i in range(1, N+1):
        print('*'+' *'*(N//2))
        print(' *'*(N//2))