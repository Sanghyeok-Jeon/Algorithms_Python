T = int(input())
for _ in range(T):
    s, p = input().split()

    cnt = s.count(p)

    print(len(s) - len(p) * cnt + cnt)