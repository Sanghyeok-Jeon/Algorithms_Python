X = int(input())
N = int(input())

calc = 0
for i in range(N):
    a, b = map(int, input().split())
    calc += a * b

if X == calc:
    print('Yes')
else:
    print('No')