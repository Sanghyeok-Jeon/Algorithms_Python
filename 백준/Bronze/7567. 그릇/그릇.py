dish = input()
pre = ''
h = 0
for d in dish:
    if d == pre:
        h += 5
    else:
        h += 10
        pre = d

print(h)