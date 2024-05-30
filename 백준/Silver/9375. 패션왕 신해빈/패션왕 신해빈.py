import sys

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    dicWear = {}

    for _ in range(n):
        wear, wearKind = sys.stdin.readline().split()

        if wearKind in dicWear.keys():
            dicWear[wearKind] += 1
        else:
            dicWear[wearKind] = 1

    ans = 1
    for w in dicWear.values():
        ans *= w + 1

    print(ans - 1)