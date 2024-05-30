T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    
    result = 0
    for n in list(map(int, input().split())):
        result += n // K
        
    print(result)