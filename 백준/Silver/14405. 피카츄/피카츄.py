s = input()
len_origin = len(s)

s = s.replace('pi', '  ')
s = s.replace('ka', '  ')
s = s.replace('chu', '   ')

if s == ' ' * len_origin:
    print('YES')
else:
    print('NO')