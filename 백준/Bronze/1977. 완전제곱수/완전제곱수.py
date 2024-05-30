M = int(input())
N = int(input())
totalSquare = []

for i in range(1, 10001):
    target = i*i
    if target > N:
        break

    if M <= target <= N:
        totalSquare.append(target)

if len(totalSquare):
    print(sum(totalSquare), totalSquare[0], sep='\n')
else:
    print(-1)