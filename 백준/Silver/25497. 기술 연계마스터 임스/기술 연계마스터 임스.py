N = int(input())
skill = input()

cnt_use_skill = 0
set_preskill = []
for s in skill:
    if s == 'S' or s == 'L':
        set_preskill.append(s)
    elif s == 'K':
        if 'S' in set_preskill:
            cnt_use_skill += 1
            set_preskill.remove('S')
        else:
            break
    elif s == 'R':
        if 'L' in set_preskill:
            cnt_use_skill += 1
            set_preskill.remove('L')
        else:
            break
    else:
        cnt_use_skill += 1

print(cnt_use_skill)