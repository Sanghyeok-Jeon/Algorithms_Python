N, K = map(int, input().split())
ggd = []
for i in range(1, K+1):
    ggd.append(int(str(N*i)[::-1]))
    
print(max(ggd))