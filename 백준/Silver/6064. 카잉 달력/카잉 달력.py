import sys

def calendarCain(M, N, x, y):
    while x <= M * N:
        if not (x - y) % N:
            return x
        x += M
    return -1

T = int(sys.stdin.readline())
for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().rstrip().split())
    print(calendarCain(M, N, x, y))