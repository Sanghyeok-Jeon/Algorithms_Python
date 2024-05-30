str1 = input()
str2 = input()

cntChar = [0] * 26
for s in str1:
    cntChar[ord(s) - 97] += 1
for s in str2:
    cntChar[ord(s) - 97] -= 1

total = 0
for c in cntChar:
    total += abs(c)

print(total)