N = int(input())
nums = list(map(int, input().split()))

cnt = 0
for i in range(1, N + 1):
    if i != nums[i - 1]:
        cnt += 1

print(cnt)