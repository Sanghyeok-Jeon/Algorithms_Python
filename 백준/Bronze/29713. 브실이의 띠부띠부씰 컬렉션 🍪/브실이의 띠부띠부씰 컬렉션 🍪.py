N = int(input())
data = input()

bsDict = {'B': 0, 'R': 0, 'O': 0, 'N': 0, 'Z': 0, 'E': 0, 'S': 0, 'I': 0, 'L': 0, 'V': 0, 'E': 0, 'R': 0}
for d in data:
    if d in bsDict:
        bsDict[d] += 1

possibleGold = N
for i in bsDict.items():
    if i[0] == 'E' or i[0] == 'R':
        possibleGold = min(i[1]//2, possibleGold)
    else:
        possibleGold = min(i[1], possibleGold)
        
print(possibleGold)