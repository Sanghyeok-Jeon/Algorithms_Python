N = int(input())
store = list(map(int, input().split()))

cnt = 0
for i in range(N):
    if store[i] == cnt % 3:
        cnt += 1
        
print(cnt)