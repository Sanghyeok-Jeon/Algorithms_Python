word = input()

line_1 = ''
line_2 = ''
line_3 = ''
line_4 = ''
line_5 = ''
for i in range(len(word)):
    if i == 0:
        line_1 += '..#..'
        line_2 += '.#.#.'
        line_3 += '#.' + word[i] + '.#'
        line_4 += '.#.#.'
        line_5 += '..#..'
    elif (i + 1) % 3:
        line_1 += '.#..'
        line_2 += '#.#.'
        line_3 += '.' + word[i] + '.#'
        line_4 += '#.#.'
        line_5 += '.#..'
    else:
        line_1 += '.*..'
        line_2 += '*.*.'
        line_3 = line_3[:-1]
        line_3 += '*.' + word[i] + '.*'
        line_4 += '*.*.'
        line_5 += '.*..'

print(line_1)
print(line_2)
print(line_3)
print(line_4)
print(line_5)