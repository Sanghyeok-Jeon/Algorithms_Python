import sys

def IntensityFunction(r, g, b):
    return 2126*r + 7152*g + 722*b

N, M = map(int, sys.stdin.readline().split())
for i in range(N):
    jData = list(map(int, sys.stdin.readline().split()))
    for j in range(M):
        R, G, B = jData[3*j], jData[3*j+1], jData[3*j+2]
        tmpRGB = IntensityFunction(R, G, B)
        if tmpRGB < 510000:
            print(chr(35), end='')
        elif 510000 <= tmpRGB < 1020000:
            print(chr(111), end='')
        elif 1020000 <= tmpRGB < 1530000:
            print(chr(43), end='')
        elif 1530000 <= tmpRGB < 2040000:
            print(chr(45), end='')
        else:
            print(chr(46), end='')
    print()