import sys
while True:
    str = sys.stdin.readline().rstrip('\n')

    if not str:
        break

    lst = [0, 0, 0, 0]
    for s in str:
        if s == ' ':
            lst[3] += 1
        elif s.isdigit():
            lst[2] += 1
        else:
            if s.islower():
                lst[0] += 1
            else:
                lst[1] += 1

    print(*lst)