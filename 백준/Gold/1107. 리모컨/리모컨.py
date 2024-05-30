import sys

def checkNum(tmpNum):
    tmpNum = str(tmpNum)
    for n in tmpNum:
        if n in btnBroken:
            return False
    return True

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
btnBroken = list(sys.stdin.readline().rstrip().split())
cntPush = abs(N - 100)

for tmpNum in range(1000001):
    if checkNum(tmpNum):
        cntPush = min(cntPush, len(str(tmpNum)) + abs(N - tmpNum))

print(cntPush)