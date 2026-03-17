s = input().strip()

q = u = a = c = 0
active = 0       
max_active = 0   
completed = 0    

for ch in s:
    if ch == 'q':
        q += 1
        active += 1
        max_active = max(max_active, active)

    elif ch == 'u':
        if q == 0:
            print(-1)
            exit()
        q -= 1
        u += 1

    elif ch == 'a':
        if u == 0:
            print(-1)
            exit()
        u -= 1
        a += 1

    elif ch == 'c':
        if a == 0:
            print(-1)
            exit()
        a -= 1
        c += 1

    elif ch == 'k':
        if c == 0:
            print(-1)
            exit()
        c -= 1
        active -= 1
        completed += 1

    else:
        print(-1)
        exit()

if q == 0 and u == 0 and a == 0 and c == 0 and completed > 0:
    print(max_active)
else:
    print(-1)