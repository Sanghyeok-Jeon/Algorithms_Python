import sys
input = sys.stdin.readline

n = int(input())
solutions = list(map(int, input().split()))

solutions.sort()

closest_sum = float('inf')
result = (0, 0, 0)

for i in range(n - 2):
    left = i + 1
    right = n - 1

    while left < right:
        current_sum = solutions[i] + solutions[left] + solutions[right]

        if abs(current_sum) < abs(closest_sum):
            closest_sum = current_sum
            result = (solutions[i], solutions[left], solutions[right])

        if current_sum < 0:
            left += 1
        elif current_sum > 0:
            right -= 1
        else:
            print(solutions[i], solutions[left], solutions[right])
            exit()

print(result[0], result[1], result[2])