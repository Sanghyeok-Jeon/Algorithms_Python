data = ''
while True:
    try:
        data += input()
    except:
        break

dicCnt = {}
for d in data:
    if d == ' ':
        continue

    if d in dicCnt:
        dicCnt[d] += 1
    else:
        dicCnt[d] = 1

result = [k for k, v in dicCnt.items() if max(dicCnt.values()) == v]

print(''.join(sorted(result)))