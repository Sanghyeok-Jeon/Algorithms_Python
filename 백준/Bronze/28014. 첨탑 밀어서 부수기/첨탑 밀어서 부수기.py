N = int(input())
H = list(map(int, input().split()))

now_h = 0
cnt = 0
for h in H:
    if h >= now_h:
        cnt += 1

    now_h = h

print(cnt)