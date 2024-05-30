N = int(input())
profile = []
for _ in range(N):
    weight, height = map(int, input().split())
    profile.append([weight, height])

for p1 in profile:
    cnt = 1
    for p2 in profile:
        if p1[0] < p2[0] and p1[1] < p2[1]:
            cnt += 1
    print(cnt, end=' ')