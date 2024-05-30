T = int(input())
for _ in range(T):
    X = input()
    xSet = set()
    for x in X:
        xSet.add(x)
        
    print(len(xSet))