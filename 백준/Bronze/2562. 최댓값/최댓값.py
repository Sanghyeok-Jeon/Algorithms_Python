maxCnt = 0
maxNum = 0
for i in range(1, 10):
    N = int(input())
    if N > maxNum:
        maxNum = N
        maxCnt = i

print(maxNum)
print(maxCnt)