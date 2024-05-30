import sys

K, N = map(int, sys.stdin.readline().split())
lanCable = [int(sys.stdin.readline()) for _ in range(K)]
left, right = 1, max(lanCable)

while left <= right:
    mid = (left + right) // 2
    cnt = 0
    for c in lanCable:
        cnt += c//mid

    if cnt < N:
        right = mid - 1
    else:
        left = mid + 1

print(right)