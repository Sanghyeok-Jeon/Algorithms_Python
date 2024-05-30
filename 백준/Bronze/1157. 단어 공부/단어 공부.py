ch = input()
cnt = [0] * 26

for c in ch:
    if ord('a') <= ord(c) <= ord('z'):
        cnt[ord(c) - ord('a')] += 1
    else:
        cnt[ord(c) - ord('A')] += 1

ans = ''
duplicate = 0
maxCnt = max(cnt)
for i in range(26):
    if cnt[i] == maxCnt:
        duplicate += 1
        ans = chr(i + ord('A'))

if duplicate > 1:
    print('?')
else:
    print(ans)