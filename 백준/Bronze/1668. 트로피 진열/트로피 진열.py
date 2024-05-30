N = int(input())
trophy = []
for _ in range(N):
    trophy.append(int(input()))
    
leftSee = 0
leftMax = 0
for i in range(N):
    if trophy[i] > leftMax:
        leftSee += 1
        leftMax = trophy[i]
        
rightSee = 0
rightMax = 0
for i in range(N-1,-1,-1):
    if trophy[i] > rightMax:
        rightSee += 1
        rightMax = trophy[i]

print(leftSee)
print(rightSee)