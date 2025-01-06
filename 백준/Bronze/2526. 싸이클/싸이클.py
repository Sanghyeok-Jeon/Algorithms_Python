N, P = map(int, input().split())

nums = set()
nums_repeat = set()
num = N
while True:
    if num in nums:
        if num in nums_repeat:
            break
        else:
            nums_repeat.add(num)

    nums.add(num)

    num = num * N % P

print(len(nums_repeat))