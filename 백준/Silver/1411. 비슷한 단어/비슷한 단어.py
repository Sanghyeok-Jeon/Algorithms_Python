import sys
input = sys.stdin.readline

n = int(input().strip())
patterns = {}

for _ in range(n):
    word = input().strip()
    mapping = {}
    next_id = 0
    pattern = []

    for ch in word:
        if ch not in mapping:
            mapping[ch] = next_id
            next_id += 1
        pattern.append(str(mapping[ch]))

    key = ','.join(pattern)
    patterns[key] = patterns.get(key, 0) + 1

ans = 0
for cnt in patterns.values():
    ans += cnt * (cnt - 1) // 2

print(ans)