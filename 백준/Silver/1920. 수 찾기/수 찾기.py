import sys

def binarySearch(A, t):
    start = 0
    end = N-1

    while start <= end:
        mid = (start + end) // 2
        if t == A[mid]:
            return 1
        elif t > A[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

A.sort()
for t in target:
    print(binarySearch(A, t))