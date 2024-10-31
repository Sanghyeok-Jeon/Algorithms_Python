N = int(input())
S = list(input().split())
s_set = set()

for s in S:
    s_set.add(s[0])
    s_set.add(s[-1])

print(1 if len(s_set) == 1 else 0)