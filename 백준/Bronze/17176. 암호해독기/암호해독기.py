N = int(input())
cryptogram = list(map(int, input().split()))
plain_text = input()

check_list = []
for pt in plain_text:
    if pt == ' ':
        check_list.append(0)
    else:
        if pt.isupper():
            check_list.append(ord(pt) - ord('A') + 1)
        else:
            check_list.append(ord(pt) - ord('a') + 27)

cryptogram.sort()
check_list.sort()

if check_list == cryptogram:
    print('y')
else:
    print('n')