import sys

def make_cantorset(s, length, start):
    if length == 1:
        return

    length //= 3
    end = start + length + length
    for i in range(start+length, end):
        s[i] = ' '

    make_cantorset(s, length, start)
    make_cantorset(s, length, end)

lines = sys.stdin.readlines()
for line in lines:
    N = int(line)
    cantorSet = ['-' for _ in range(3**N)]
    make_cantorset(cantorSet, len(cantorSet), 0)
    print(''.join(cantorSet))