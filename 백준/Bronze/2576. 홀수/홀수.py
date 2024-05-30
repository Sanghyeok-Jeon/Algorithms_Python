listNum = [int(input()) for _ in range(7)]
listNum.sort()

sumOdd = 0
minOdd = -1
for n in listNum:
    if n % 2:
        if minOdd == -1:
            minOdd = n
        sumOdd += n
        
if minOdd == -1:
    print(minOdd)
else:
    print(sumOdd)
    print(minOdd)