N = int(input())
for _ in range(N):
    data = set(list(input()))
    sumNotAppear = ord('Z')*(ord('Z')+1)//2 - (ord('A')-1)*ord('A')//2
    for d in data:
        sumNotAppear -= ord(d)
    print(sumNotAppear)