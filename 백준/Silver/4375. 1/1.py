import sys

for line in sys.stdin:
    line = line.strip()
    if not line:
        break

    n = int(line)

    rem = 1
    length = 1

    while rem % n != 0:
        rem = (rem * 10 + 1) % n
        length += 1

    print(length)