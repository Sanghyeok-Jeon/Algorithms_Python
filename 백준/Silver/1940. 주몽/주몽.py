def count_pairs(n, m, materials):
    left = 0
    right = n - 1
    count = 0

    while left < right:
        current_sum = materials[left] + materials[right]

        if current_sum == m:
            count += 1
            left += 1
            right -= 1
        elif current_sum < m:
            left += 1
        else:
            right -= 1

    return count

N = int(input())
M = int(input())
materials = sorted(list(map(int, input().split())))

if N == 0:
    print(0)
else:
    print(count_pairs(N, M, materials))