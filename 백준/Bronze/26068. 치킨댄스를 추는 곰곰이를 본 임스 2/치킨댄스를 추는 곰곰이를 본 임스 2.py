N = int(input())
cnt = 0
for _ in range(N):
    D, day = input().split('-')
    
    if int(day) <= 90:
        cnt += 1
        
print(cnt)