target = int(input())
cnt = 0
for n in list(map(int, input().split())):
    if target == n:
        cnt += 1

print(cnt)