import sys

input = sys.stdin.readline

N, M = map(int, input().split())
wordDict = dict()
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M:
        if word in wordDict:
            wordDict[word][0] += 1
        else:
            wordDict[word] = [1, len(word), word]

wordList = sorted(wordDict.items(), key= lambda x: (-x[1][0], -x[1][1], x[1][2]))

for w in wordList:
    print(w[0])