N = int(input())
cardData = list(map(int, input().split()))
M = int(input())
target = list(map(int, input().split()))

dictCard = dict()

for card in cardData:
    try:
        dictCard[card] += 1
    except:
        dictCard[card] = 1

for t in target:
    try:
        print(dictCard[t], end=' ')
    except:
        print(0, end=' ')