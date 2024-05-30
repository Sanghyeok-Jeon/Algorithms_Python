h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

if h1==h2 and m1==m2 and s1==s2:
    print('24:00:00')
else:
    hh, mm, ss = h2-h1, m2-m1, s2-s1
    if ss < 0:
        ss += 60
        mm -= 1
    if mm < 0:
        mm += 60
        hh -= 1
    if hh < 0:
        hh += 24
    print('{0:02d}:{1:02d}:{2:02d}'.format(hh, mm, ss))