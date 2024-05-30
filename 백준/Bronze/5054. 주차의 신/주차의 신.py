t = int(input())
for _ in range(t):
    n = int(input())
    store = sorted(list(map(int, input().split())))
    middle = (store[0] + store[-1]) // 2
    
    walking = 0
    for i in range(1, n):
        walking += store[i] - store[i-1]
    
    walking += store[-1] - store[0]
        
    print(walking)