def CntLOVE(data, dicData):
    for s in data:
        if s == 'L':
            dicData['L'] += 1
        elif s == 'O':
            dicData['O'] += 1
        elif s == 'V':
            dicData['V'] += 1
        elif s == 'E':
            dicData['E'] += 1
    return

def CalLOVE(dicHost, dicGuest):
    LO = (dicHost['L'] + dicGuest['L']) + (dicHost['O'] + dicGuest['O'])
    LV = (dicHost['L'] + dicGuest['L']) + (dicHost['V'] + dicGuest['V'])
    LE = (dicHost['L'] + dicGuest['L']) + (dicHost['E'] + dicGuest['E'])
    OV = (dicHost['O'] + dicGuest['O']) + (dicHost['V'] + dicGuest['V'])
    OE = (dicHost['O'] + dicGuest['O']) + (dicHost['E'] + dicGuest['E'])
    VE = (dicHost['V'] + dicGuest['V']) + (dicHost['E'] + dicGuest['E'])

    return (LO * LV * LE * OV * OE * VE) % 100

host = input()
cntLoveHost = {'L':0, 'O':0, 'V':0, 'E':0}
CntLOVE(host, cntLoveHost)

N = int(input())
lstGuest = [input() for _ in range(N)]
lstGuest.sort()
calLove = -1
selectedGuest = ''
for i in range(N):
    guest = lstGuest[i]
    cntLoveGuest = {'L':0, 'O':0, 'V':0, 'E':0}
    CntLOVE(guest, cntLoveGuest)

    tmpCalLove = CalLOVE(cntLoveHost, cntLoveGuest)
    if tmpCalLove > calLove:
        calLove = tmpCalLove
        selectedGuest = guest

print(selectedGuest)