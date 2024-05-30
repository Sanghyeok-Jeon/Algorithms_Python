import sys

T = int(sys.stdin.readline())

funScore = 0
for i in range(T):
    l, r = map(int, sys.stdin.readline().split())
    
    if i:
        if l != 0 and l == prevL:
            funScore += 1
    
        if r != 0 and r == prevR:
            funScore += 1
        
    if l != 0 and l == r:
        funScore += 1
        
    prevL, prevR = l, r
    
print(funScore)
    