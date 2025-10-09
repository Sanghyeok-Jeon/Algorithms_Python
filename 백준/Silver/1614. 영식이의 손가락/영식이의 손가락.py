import sys

finger = int(sys.stdin.readline())
count = int(sys.stdin.readline())

if finger == 1:
    result = count * 8
elif finger == 5:
    result = count * 8 + 4
else:
    if count % 2 == 0:
        result = 4 * count + (finger - 1)
    else:
        result = 4 * count + (5 - finger)

print(result)