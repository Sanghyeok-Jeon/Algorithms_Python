import sys

for tc in range(int(sys.stdin.readline())):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    print('Case #{}: {}'.format(tc+1, A+B))