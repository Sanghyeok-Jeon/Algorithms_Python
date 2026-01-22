import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = list(map(int, input().split()))

left = 0
odd = 0
even = 0
ans = 0

for right in range(N):
    if arr[right] % 2 == 0:
        even += 1
    else:
        odd += 1

    while odd > K:
        if arr[left] % 2 == 0:
            even -= 1
        else:
            odd -= 1
        left += 1

    ans = max(ans, even)

print(ans)
