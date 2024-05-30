N, K = map(int, input().split())
nums = list(map(int, input().split(',')))
for _ in range(K):
    nums = [nums[i+1]-nums[i] for i in range(len(nums)-1)]

print(*nums, sep=',')