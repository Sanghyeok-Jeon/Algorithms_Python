while True:
    password = input()

    if password == 'end':
        break

    vowel = ['a', 'e', 'i', 'o', 'u']
    cnt_vowel_repeat = 0
    cnt_consonant_repeat = 0
    vowel_exist = False
    acceptable = True
    for i in range(len(password)):
        if password[i] in vowel:
            vowel_exist = True
            cnt_vowel_repeat += 1
            cnt_consonant_repeat = 0

            if cnt_vowel_repeat == 3:
                acceptable = False
                break
        else:
            cnt_vowel_repeat = 0
            cnt_consonant_repeat += 1

            if cnt_consonant_repeat == 3:
                acceptable = False
                break

        if i > 0:
            if password[i] == password[i - 1]:
                if password[i] not in ('e', 'o'):
                    acceptable = False
                    break

    if not vowel_exist or not acceptable:
        print('<{}> is not acceptable.'.format(password))
    else:
        print('<{}> is acceptable.'.format(password))