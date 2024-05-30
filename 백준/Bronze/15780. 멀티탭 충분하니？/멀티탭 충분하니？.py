N, K = map(int, input().split())
maxPossible = 0
for mt in map(int, input().split()):
    maxPossible += mt//2 + 1 if mt % 2 else mt//2

print('YES' if N <= maxPossible else 'NO')