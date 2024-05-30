N = int(input())
numList = list(map(int, input().split()))

M = max(numList)
sumNum = 0
for i in range(N):
    sumNum += numList[i] / M * 100

print('{:.3f}'.format(sumNum/N))