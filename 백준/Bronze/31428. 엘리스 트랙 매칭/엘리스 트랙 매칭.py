N = int(input())
friends = list(input().split())
hellobit = input()

cnt = 0
for f in friends:
    if f == hellobit:
        cnt += 1

print(cnt)