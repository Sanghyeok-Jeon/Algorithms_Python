N, K = map(int, input().split())
for i in range(N):
    A, B = map(int, input().split())
    K += A - B
    
print('비와이')