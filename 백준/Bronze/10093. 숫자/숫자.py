A, B = map(int, input().split())
nums = [num for num in range(A+1, B)] if A < B else [num for num in range(B+1, A)]
print(len(nums))
print(*nums)