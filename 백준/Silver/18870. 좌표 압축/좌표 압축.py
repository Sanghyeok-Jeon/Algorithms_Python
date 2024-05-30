import sys

N = int(sys.stdin.readline())
X = list(map(int, sys.stdin.readline().rstrip().split()))

sortSetX = list(sorted(set(X)))

dictX = {sortSetX[i]:i for i in range(len(sortSetX))}

print(*[dictX[x] for x in X])