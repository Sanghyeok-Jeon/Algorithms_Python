R, B = map(int, input().split())

L, W = 0, 0
for i in range(1, R+1):
    for j in range(1, R+1):
        if (i-2)*(j-2) == B and (i*2 + (j-2)*2) == R:
           L, W = max(i, j), min(i, j)
           break
    if L:
        break
       
print(L, W)