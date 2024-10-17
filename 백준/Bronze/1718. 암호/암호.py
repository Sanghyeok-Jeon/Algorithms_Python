pt = input()
crypto = input()

for i in range(len(pt)):
    if pt[i] == ' ':
        print(' ', end='')
    else:
        if ord(pt[i]) - (ord(crypto[i % len(crypto)]) + 1) >= 0:
            print(chr((ord(pt[i]) - (ord(crypto[i % len(crypto)]) + 1)) + ord('a')), end='')
        else:
            print(chr(ord('z') + (ord(pt[i]) - (ord(crypto[i % len(crypto)]) + 1)) + 1), end='')