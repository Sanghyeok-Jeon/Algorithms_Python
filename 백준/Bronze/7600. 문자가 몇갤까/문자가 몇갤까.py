while True:
    target = input().upper()
    if target == '#':
        break
    
    cntChr = set()
    for t in target:
        if ord('A') <= ord(t) <= ord('Z'):
            cntChr.add(t)
    
    print(len(cntChr))