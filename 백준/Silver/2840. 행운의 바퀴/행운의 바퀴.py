import sys

n, k = map(int, input().split())

wheel = ['?'] * n
arrow = 0
used = [False] * 26

possible = True

for _ in range(k):
    s, c = input().split()
    s = int(s)
    arrow = (arrow - s) % n

    if wheel[arrow] != '?':
        if wheel[arrow] != c:
            possible = False
            break
    else:
        if used[ord(c) - ord('A')]:
            possible = False
            break
            
        wheel[arrow] = c
        used[ord(c) - ord('A')] = True

if not possible:
    print("!")
else:
    result = []
    for i in range(arrow, arrow + n):
        ch = wheel[i % n]
        result.append(ch)
    print("".join(result))
