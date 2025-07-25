def solve(s):
    set_p = set()
    set_k = set()
    set_h = set()
    set_t = set()

    for i in range(0, len(s), 3):
        card = s[i:i + 3]
        symbol = card[0]
        number = card[1:]

        if symbol == 'P':
            if number in set_p:
                return 'GRESKA'
            else:
                set_p.add(number)
        elif symbol == 'K':
            if number in set_k:
                return 'GRESKA'
            else:
                set_k.add(number)
        elif symbol == 'H':
            if number in set_h:
                return 'GRESKA'
            else:
                set_h.add(number)
        else:
            if number in set_t:
                return 'GRESKA'
            else:
                set_t.add(number)

    result = [str(13 - len(set_p)), str(13 - len(set_k)), str(13 - len(set_h)), str(13 - len(set_t))]

    return ' '.join(result)

S = input()

print(solve(S))