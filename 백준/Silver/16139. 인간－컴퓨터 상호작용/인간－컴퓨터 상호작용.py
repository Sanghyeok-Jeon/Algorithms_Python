import sys

input = sys.stdin.readline

s = input().strip()
q = int(input())

prefix = [[0] * 26 for _ in range(len(s) + 1)]

for i in range(len(s)):
    for j in range(26):
        prefix[i + 1][j] = prefix[i][j]
    prefix[i + 1][ord(s[i]) - ord('a')] += 1

for _ in range(q):
    a, l, r = input().split()
    l, r = int(l), int(r)
    idx = ord(a) - ord('a')
    print(prefix[r + 1][idx] - prefix[l][idx])