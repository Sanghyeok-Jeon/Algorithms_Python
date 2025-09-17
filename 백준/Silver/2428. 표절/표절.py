import sys
input = sys.stdin.readline

N = int(input())
file_sizes = sorted(list(map(int, input().split())))

count = 0
for i in range(N):
    left = i
    right = N - 1

    while left <= right:
        mid = (left + right) // 2

        if file_sizes[i] >= 0.9 * file_sizes[mid]:
            left = mid + 1
        else:
            right = mid - 1

    count += left - i - 1

print(count)