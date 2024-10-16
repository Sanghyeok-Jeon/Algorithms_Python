days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
luna_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while True:
    dd, mm, yyyy = map(int, input().split())
    if dd == 0:
        break

    luna_flag = False
    total_days = 0
    if yyyy % 4 == 0:
        if yyyy % 100 != 0 or yyyy % 400 == 0:
            luna_flag = True

    if luna_flag:
        if mm > 1:
            total_days += sum(luna_days[:mm - 1])
        total_days += dd
    else:
        if mm > 1:
            total_days += sum(days[:mm - 1])
        total_days += dd

    print(total_days)