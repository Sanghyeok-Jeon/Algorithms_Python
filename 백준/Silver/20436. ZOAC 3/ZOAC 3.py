Sl, Sr = input().split()
data = input()

consonant = {
    'q': (0, 0), 'w': (0, 1), 'e': (0, 2), 'r': (0, 3), 't': (0, 4),
    'a': (1, 0), 's': (1, 1), 'd': (1, 2), 'f': (1, 3), 'g': (1, 4),
    'z': (2, 0), 'x': (2, 1), 'c': (2, 2), 'v': (2, 3)
}
vowel = {
    'y': (0, 1), 'u': (0, 2), 'i': (0, 3), 'o': (0, 4), 'p': (0, 5),
    'h': (1, 1), 'j': (1, 2), 'k': (1, 3), 'l': (1, 4),
    'b': (2, 0), 'n': (2, 1), 'm': (2, 2)
}

total = 0
for d in data:
    if d in consonant.keys():
        sl_x, sl_y = consonant[Sl]
        nl_x, nl_y = consonant[d]

        total += abs(sl_x - nl_x) + abs(sl_y - nl_y)
        total += 1

        Sl = d
    else:
        sr_x, sr_y = vowel[Sr]
        nr_x, nr_y = vowel[d]

        total += abs(sr_x - nr_x) + abs(sr_y - nr_y)
        total += 1

        Sr = d

print(total)

