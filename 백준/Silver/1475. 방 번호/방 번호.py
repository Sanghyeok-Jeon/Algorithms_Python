listNum = list(map(int, input()))
cntNum = [0] * 9

for n in listNum:
    if n in (6, 9):
        cntNum[6] += 1
    else:
        cntNum[n] += 1

cntNum[6] = cntNum[6]//2 + 1 if cntNum[6]%2 else cntNum[6]//2

print(max(cntNum))