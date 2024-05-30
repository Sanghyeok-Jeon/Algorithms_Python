def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)

n = int(input())
nums = list(map(int, input().split()))

g = gcd(nums[0], gcd(nums[1], nums[-1]))
divisor = set()
for i in range(1, int(g**0.5) + 1):
    if not g % i:
        divisor.add(i)
        divisor.add(g // i)

for d in sorted(divisor):
    print(d)