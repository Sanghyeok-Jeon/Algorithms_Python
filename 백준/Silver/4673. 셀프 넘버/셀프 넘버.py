selfNumber = set(range(1, 10001))
generatorNumber = set()

for n in range(1, 10001):
    for sNum in str(n):
        n += int(sNum)
    generatorNumber.add(n)

print(*sorted(selfNumber-generatorNumber), sep='\n')