import sys
input = sys.stdin.readline

n = int(input())
ext_cnt = {}

for _ in range(n):
    name, ext = input().strip().split('.')
    if ext in ext_cnt:
        ext_cnt[ext] += 1
    else:
        ext_cnt[ext] = 1

for ext in sorted(ext_cnt.keys()):
    print(ext, ext_cnt[ext])