N = int(input())
logo = list(input())

cnt_alpha = [0] * 26
for l in logo:
    if l.isalpha():
        cnt_alpha[ord(l) - ord('a')] += 1

print(max(cnt_alpha))