N = int(input())

claps = 0
for i in range(1, N + 1):
    nums = list(str(i))
    for n in nums:
        if not int(n) % 3 and int(n) != 0:
            claps += 1
            
print(claps)