def gcd(a, b):
    while b > 0:
        a, b = b, a % b

    return a

N = int(input())
for _ in range(N):
    nums = list(map(int, input().split()))
    nums.sort(reverse=True)

    max_gcd = 0
    for i in range(len(nums) - 1):
        for j in range(i + 1, len(nums)):
            tmp_gcd = gcd(nums[i], nums[j])

            max_gcd = max(max_gcd, tmp_gcd)

    print(max_gcd)