T = int(input())

calA = T // 300
A = calA if calA else 0
T %= 300

calB = T // 60
B = calB if calB else 0
T %= 60

calC = T // 10
C = calC if calC else 0
T %= 10

if T:
    print(-1)
else:
    print(A, B, C)