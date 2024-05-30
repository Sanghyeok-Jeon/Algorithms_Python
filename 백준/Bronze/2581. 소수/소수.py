M = int(input())
N = int(input())

sosu = [1] * (N+1)

for i in range(N+1):
    if i < 2:
        sosu[i] = 0
    else:
        for j in range(i*2, N+1, i):
            sosu[j] = 0

first = 0
sumSosu = 0
for i in range(M, N+1):
    if sosu[i] == 1:
        if first == 0:
            first = i
        sumSosu += i

if sumSosu == 0:
    print(-1)
else:
    print(sumSosu)
    print(first)