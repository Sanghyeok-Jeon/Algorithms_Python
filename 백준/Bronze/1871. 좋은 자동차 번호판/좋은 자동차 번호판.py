N = int(input())
for _ in range(N):
    firstPart, secondPart = input().split('-')
    totalFP = 26*26*(ord(firstPart[0])-ord('A')) + 26 * (ord(firstPart[1])-ord('A')) + (ord(firstPart[2])-ord('A'))

    if abs(totalFP - int(secondPart)) <= 100:
        print('nice')
    else:
        print('not nice')