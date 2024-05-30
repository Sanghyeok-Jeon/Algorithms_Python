N = int(input())
guest = list(map(int, input().split()))
pcNo = [0] * 101

rejectGuest = 0
for g in guest:
    if pcNo[g]:
        rejectGuest += 1
    else:
        pcNo[g] = 1

print(rejectGuest)