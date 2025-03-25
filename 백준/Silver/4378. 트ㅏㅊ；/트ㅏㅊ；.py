line_number = ['`', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '=']
line_first = ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', '\\']
line_second = ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';', '\'']
line_third = ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']

while True:
    try:
        data = input()
        for d in data:
            if d == ' ':
                print(' ', end='')
            else:
                if d in line_number:
                    idx = line_number.index(d)
                    print(line_number[idx - 1], end='')
                elif d in line_first:
                    idx = line_first.index(d)
                    print(line_first[idx - 1], end='')
                elif d in line_second:
                    idx = line_second.index(d)
                    print(line_second[idx - 1], end='')
                else:
                    idx = line_third.index(d)
                    print(line_third[idx - 1], end='')
        print()
    except:
        exit(0)