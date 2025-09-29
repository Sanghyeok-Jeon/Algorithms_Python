import sys
input = sys.stdin.readline

def is_surprising(s):
    l = len(s)

    for d in range(1, l):
        pairs = set()
        for i in range(l - d):
            pair = (s[i], s[i + d])
            if pair in pairs:
                return False

            pairs.add(pair)

    return True

while True:
    s = input().strip()
    if s == '*':
        break

    if is_surprising(s):
        print('{} is surprising.'.format(s))
    else:
        print('{} is NOT surprising.'.format(s))