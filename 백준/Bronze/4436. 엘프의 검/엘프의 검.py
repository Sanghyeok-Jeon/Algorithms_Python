import sys

while True:
    try:
        n = int(input())
    except:
        break

    appeared = set()

    k = 0
    while len(appeared) != 10:
        k += 1
        tmpSword = n * k

        for s in str(tmpSword):
            if s not in appeared:
                appeared.add(s)

    print(k)