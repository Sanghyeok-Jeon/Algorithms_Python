from itertools import permutations

x = input()
int_x = int(x)
nums = sorted(set(int(''.join(p)) for p in permutations(x)))

for num in nums:
    if num > int_x:
        print(num)
        break
else:
    print(0)