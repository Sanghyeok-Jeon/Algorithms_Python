N = int(input())
sumPoint = 0
for i in range(N+1):
    for j in range(i, N+1):
        sumPoint += i + j
print(sumPoint)