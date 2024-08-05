n = int(input())
for i in range(1, n + 1):
    print('String #{}'.format(i))
    S = input()
    for s in S:
        print(chr(ord(s) + 1 if s != 'Z' else ord('A')), end='')
    print()
    print()