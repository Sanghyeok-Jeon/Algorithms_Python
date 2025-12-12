def previous_permutation(seq):
    i = len(seq) - 1
    while i > 0 and seq[i - 1] <= seq[i]:
        i -= 1

    if i <= 0:
        return False

    j = len(seq) - 1
    while seq[j] >= seq[i - 1]:
        j -= 1

    seq[i - 1], seq[j] = seq[j], seq[i - 1]

    seq[i:] = seq[i:][::-1]

    return True

import sys
input = sys.stdin.readline

n = int(input())
seq = list(map(int, input().split()))

if previous_permutation(seq):
    print(' '.join(map(str, seq)))
else:
    print(-1)