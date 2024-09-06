N, M = map(int, input().split())

cnt = N
group_M = N
while group_M:
    group_M //= M
    cnt += group_M

print(cnt)
