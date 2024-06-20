def count_unique_subarrays(arr):
    n = len(arr)
    seen = set()
    left = 0
    count = 0

    for right in range(n):
        while arr[right] in seen:
            seen.remove(arr[left])
            left += 1

        seen.add(arr[right])
        count += (right - left + 1)

    return count

n = int(input())
arr = list(map(int, input().split()))

print(count_unique_subarrays(arr))