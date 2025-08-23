N, K = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)

print(sum(nums[:K]) - sum(range(K)))