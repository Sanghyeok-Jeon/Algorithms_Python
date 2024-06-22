n = int(input())
S = input()

dict_uospc = {'u':0, 'o':0, 's':0, 'p':0, 'c':0}

for s in S:
    if s in dict_uospc:
        dict_uospc[s] += 1

print(min(dict_uospc.values()))