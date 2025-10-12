n = int(input())
s = input().strip()

b_groups = 0
r_groups = 0
prev = ''
for ch in s:
    if ch != prev:
        if ch == 'B':
            b_groups += 1
        else:
            r_groups += 1
    prev = ch

print(min(b_groups, r_groups) + 1)