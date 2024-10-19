while True:
    S = input()

    if S == 'EOI':
        break

    if 'NEMO' in S.upper():
        print('Found')
    else:
        print('Missing')