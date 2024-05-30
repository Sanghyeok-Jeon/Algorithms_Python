total = 0
numDict = {}
for _ in range(10):
    num = int(input())

    total += num

    if num in numDict:
        numDict[num] += 1
    else:
        numDict[num] = 1

print(total // 10)
print(sorted(numDict.items(), key=lambda x: -x[1])[0][0])