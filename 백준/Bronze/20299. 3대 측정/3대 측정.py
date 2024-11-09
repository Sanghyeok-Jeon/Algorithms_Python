import sys
input = sys.stdin.readline

N, K, L = map(int, input().split())

vip_team_cnt = 0
vip_members = []
for _ in range(N):
    X = list(map(int, input().split()))

    tmp_members = []
    for x in X:
        if x >= L:
            tmp_members.append(x)
        else:
            break

    if len(tmp_members) == 3 and sum(tmp_members) >= K:
        vip_members += tmp_members
        vip_team_cnt += 1

print(vip_team_cnt)
print(*vip_members)