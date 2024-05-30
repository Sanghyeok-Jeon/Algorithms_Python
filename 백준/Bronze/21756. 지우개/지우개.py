N = int(input())
nums = [0] + list(range(1, N+1))
while True:
    if len(nums) == 2:
        break
    
    nums = nums[::2]

print(nums[1])