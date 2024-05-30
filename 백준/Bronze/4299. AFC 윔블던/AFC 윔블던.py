S, D = map(int, input().split())

if not (S+D)%2 and not (S-D)%2:
    A = (S + D) // 2
    B = (S - D) // 2
    if A >= 0 and B >= 0:
        print('{} {}'.format(A, B) if A > B else '{} {}'.format(B, A))
    else:
        print(-1)
else:
    print(-1)