n = int(input())
s = input()

if s.count('2') > s.count('e'):
    print('2')
elif s.count('2') < s.count('e'):
    print('e')
else:
    print('yee')