N = int(input())

groupWord = 0
for _ in range(N):
    targetWord = input()
    alreadySet = set()
    targetOK = True
    for i in range(len(targetWord)):
        if targetWord[i] not in alreadySet:
            alreadySet.add(targetWord[i])
        else:
            if targetWord[i-1] == targetWord[i]:
                continue
            else:
                targetOK = False
                break

    if targetOK:
        groupWord += 1

print(groupWord)