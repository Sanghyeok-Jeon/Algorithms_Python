N = int(input())
S = input()
if S.count('s') > S.count('b'):
    print('security!')
elif S.count('s') < S.count('b'):
    print('bigdata?')
else:
    print('bigdata? security!')