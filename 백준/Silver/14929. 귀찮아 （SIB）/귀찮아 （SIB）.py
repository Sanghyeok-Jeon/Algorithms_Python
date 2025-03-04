import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))

sum_temp = sum(nums)
answer = 0
for i in range(n - 1):
    sum_temp -= nums[i]
    answer += sum_temp * nums[i]

print(answer)