while True:
    data = input()
    if data == '#':
        break

    vowels = 'aeiou'

    if data[0] not in vowels:
        back_word = ''
        for i in range(len(data)):
            if data[i] in vowels:
                data = data[i:] + data[:i]

    print(data + 'ay')