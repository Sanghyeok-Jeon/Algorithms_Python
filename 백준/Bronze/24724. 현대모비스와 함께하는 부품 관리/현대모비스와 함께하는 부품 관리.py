import sys
input = sys.stdin.readline

T = int(input())
for i in range(1, T + 1):
    N = int(input())
    A, B = map(int, input().split())
    for _ in range(N):
        a, b = map(int, input().split())

    print('Material Management {}'.format(i))
    print('Classification ---- End!')