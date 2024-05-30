data = input()
cntJOI, cntIOI = 0, 0
for i in range(len(data)-2):
    if data[i:i+3] == 'JOI':
        cntJOI += 1
    if data[i:i+3] == 'IOI':
        cntIOI += 1

print(cntJOI, cntIOI, sep='\n')