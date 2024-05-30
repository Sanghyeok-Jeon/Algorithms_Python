S = input()

mobis = [0] * 5
for s in S:
    if s == 'M':
        mobis[0] += 1
    elif s == 'O':
        mobis[1] += 1
    elif s == 'B':
        mobis[2] += 1
    elif s == 'I':
        mobis[3] += 1
    elif s == 'S':
        mobis[4] += 1

print('YES' if sorted(mobis)[0] else 'NO')