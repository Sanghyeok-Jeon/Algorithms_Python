alphabet = [0] * 26
S = input()
for s in S:
    alphabet[ord(s)-ord('a')] += 1

print(*alphabet)