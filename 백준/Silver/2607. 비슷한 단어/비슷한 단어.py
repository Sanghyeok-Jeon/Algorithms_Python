import sys
input = sys.stdin.readline

n = int(input().strip())
base_word = input().strip()

base = [0] * 26
for ch in base_word:
    base[ord(ch) - 65] += 1

ans = 0

for _ in range(n - 1):
    word = input().strip()
    temp = base[:] 
    extra = 0

    for ch in word:
        idx = ord(ch) - 65
        if temp[idx] > 0:
            temp[idx] -= 1
        else:
            extra += 1

    left = sum(temp)

    if (left == 0 and extra == 0) or (left == 1 and extra == 0) or (left == 0 and extra == 1) or (left == 1 and extra == 1):
        ans += 1

print(ans)