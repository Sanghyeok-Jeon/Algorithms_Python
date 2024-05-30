S = input()
alphabet = [-1] * 26
for i in range(len(S)):
    ch = S[i]
    if alphabet[ord(ch)-ord('a')] == -1:
        alphabet[ord(ch)-ord('a')] = i

print(*alphabet)