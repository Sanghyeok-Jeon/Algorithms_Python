import sys

N = int(sys.stdin.readline())
listOrder = list(map(int, sys.stdin.readline().split()))

listOrder.sort()

for i in range(1, N):
    listOrder[i] += listOrder[i-1]

print(sum(listOrder))