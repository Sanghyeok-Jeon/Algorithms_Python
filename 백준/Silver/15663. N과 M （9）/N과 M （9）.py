from itertools import permutations

N, M = map(int, input().split())
numList = sorted(list(map(int, input().split())))
numList.sort()

result = []
for numbers in list(permutations(numList, M)):
    result.append(numbers)

for rs in sorted(list(set(result))):
    print(*rs)