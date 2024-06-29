N = int(input())
S = list(map(int, input().split()))

max_cnt = 0
now_cnt = 0
for s in S:
    if s == 0:
        max_cnt = max(max_cnt, now_cnt)
        now_cnt = 0
    else:
        now_cnt += 1
max_cnt = max(max_cnt, now_cnt)

print(max_cnt)