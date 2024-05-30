data = list(input().split())
noList = ['i', 'pa', 'te', 'ni', 'niti', 'a', 'ali', 'nego', 'no', 'ili']
result = ''
for i in range(len(data)):
    if i != 0:
        if data[i] in noList:
            continue
    result += data[i][0]

print(result.upper())