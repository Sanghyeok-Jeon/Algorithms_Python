N = int(input())
cardNum = set(map(int, input().split()))
M = int(input())
cardDummy = list(map(int, input().split()))

result = [0] * M
for i in range(M):
    if cardDummy[i] in cardNum:
        result[i] = 1

print(*result)