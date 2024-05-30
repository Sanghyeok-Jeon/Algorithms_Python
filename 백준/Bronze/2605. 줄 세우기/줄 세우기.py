N = int(input())
chooseNum = list(map(int, input().split()))

newLine = []
i = 1
for c in chooseNum:
    newLine.insert(c, i)
    i += 1

print(*newLine[::-1])