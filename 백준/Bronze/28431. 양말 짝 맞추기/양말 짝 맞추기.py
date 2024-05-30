result = 0
nums = set()
for _ in range(5):
    num = int(input())
    if num in nums:
        result -= num
        nums.remove(num)
    else:
        result += num
        nums.add(num)

print(result)