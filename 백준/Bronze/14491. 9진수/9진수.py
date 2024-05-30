T = int(input())
nineJS = 0

cnt = 0
while T > 0:
    nineJS += T%9 * 10**cnt
    T //= 9
    cnt += 1

print(nineJS)