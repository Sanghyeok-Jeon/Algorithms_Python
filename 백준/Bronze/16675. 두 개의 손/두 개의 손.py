Ml, Mr, Tl, Tr = input().split()

# 둘 다 양손이 다른 경우
if Ml != Mr and Tl != Tr:
    print('?')

# 민성이만 양손이 같은 경우
elif Ml == Mr and Tl != Tr:
    if Ml == 'R' and (Tl == 'P' or Tr == 'P'):
        print('TK')
    elif Ml == 'P' and (Tl == 'S' or Tr == 'S'):
        print('TK')
    elif Ml == 'S' and (Tl == 'R' or Tr == 'R'):
        print('TK')
    else:
        print('?')

# 태경이만 양손이 같은 경우
elif Ml != Mr and Tl == Tr:
    if Tl == 'R' and (Ml == 'P' or Mr == 'P'):
        print('MS')
    elif Tl == 'P' and (Ml == 'S' or Mr == 'S'):
        print('MS')
    elif Tl == 'S' and (Ml == 'R' or Mr == 'R'):
        print('MS')
    else:
        print('?')

# 둘 다 양손이 같은 경우
else:
    if Ml == 'R':
        if Tl == 'R':
            print('?')
        elif Tl == 'P':
            print('TK')
        else:
            print('MS')
    elif Ml == 'P':
        if Tl == 'R':
            print('MS')
        elif Tl == 'P':
            print('?')
        else:
            print('TK')
    else:
        if Tl == 'R':
            print('TK')
        elif Tl == 'P':
            print('MS')
        else:
            print('?')