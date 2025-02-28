while True:
    try:
        S, T = input().split()
        list_s = list(S)
        for t in T:
            if list_s and t == list_s[0]:
                list_s.pop(0)

        if not list_s:
            print('Yes')
        else:
            print('No')
    except:
        break