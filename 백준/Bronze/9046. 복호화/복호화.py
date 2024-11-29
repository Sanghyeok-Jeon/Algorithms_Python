T = int(input())
for _ in range(T):
    S = input()
    dict_s = {}

    for s in S:
        if s.isalpha():
            if s in dict_s:
                dict_s[s] += 1
            else:
                dict_s[s] = 1

    if list(dict_s.values()).count(max(dict_s.values())) > 1:
        print('?')
    else:
        print(sorted(list(dict_s.items()), key=lambda x:-x[1])[0][0])