T = int(input())
for _ in range(T):
    n = int(input())
    
    maxNum = n
    while True:
        if n == 1:
            print(maxNum)
            break
        
        if n % 2:
            n = n * 3 + 1
        else:
            n //= 2
            
        maxNum = max(maxNum, n)