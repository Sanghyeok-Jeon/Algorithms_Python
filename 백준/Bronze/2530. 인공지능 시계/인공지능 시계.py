A, B, C = map(int, input().split())
D = int(input())
D += A*3600 + B*60 + C

newA = D//3600%24
newB = (D%3600)//60
newC = D%60

print('{} {} {}'.format(newA, newB, newC))