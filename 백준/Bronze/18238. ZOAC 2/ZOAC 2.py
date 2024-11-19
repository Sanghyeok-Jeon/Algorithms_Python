S = input()

time = 0
now_alpha = 'A'
for s in S:
    left = ord(s) - ord(now_alpha)
    right = ord(now_alpha) - ord(s)

    left = left if left >= 0 else 26 + left
    right = right if right >= 0 else 26 + right

    time += min(left, right)

    now_alpha = s

print(time)