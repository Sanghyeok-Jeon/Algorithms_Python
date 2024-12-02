T = int(input())
for _ in range(T):
    S = input()

    if len(S) % 2:
        S += S

    before = ''
    after = ''
    for i in range(len(S)):
        if not i % 2:
            before += S[i]
        else:
            after += S[i]

    print(before)
    print(after)