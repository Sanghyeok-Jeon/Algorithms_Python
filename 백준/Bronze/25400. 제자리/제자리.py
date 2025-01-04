N = int(input())
A = list(map(int, input().split()))

x = 1
cnt = 0
for a in A:
    if a == x:
        x += 1
    else:
        cnt += 1

print(cnt)