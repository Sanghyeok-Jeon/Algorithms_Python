import sys
input = sys.stdin.readline

N, K, B = map(int, input().split())
broken = [0] * (N + 1)  # 1-indexed
for _ in range(B):
    idx = int(input().strip())
    broken[idx] = 1

cur = sum(broken[1:K+1])
ans = cur

for i in range(K + 1, N + 1):
    cur += broken[i]        
    cur -= broken[i - K]   
    if cur < ans:
        ans = cur

print(ans)