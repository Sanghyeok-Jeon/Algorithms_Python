N = int(input())
nums = list(map(int, input().split()))

total_sum = sum(nums)
result = 0
for num in nums:
    result += num * (total_sum - num)

print(result // 2)