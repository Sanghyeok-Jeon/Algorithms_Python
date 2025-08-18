import sys
input = sys.stdin.readline

def lower_bound(target):
    start = 0
    end = N - 1

    while start <= end:
        mid = (start + end) // 2

        if A[mid] < target:
            start = mid + 1
        elif A[mid] > target:
            end = mid - 1
        elif A[mid] == target:
            if end == mid:
                break
            end = mid

    if A[end] == target:
        return end
    else:
        return -1

N, M = map(int, input().split())
A = sorted([int(input()) for _ in range(N)])

for _ in range(M):
    target = int(input())
    print(lower_bound(target))