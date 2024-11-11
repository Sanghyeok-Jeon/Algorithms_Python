T = int(input())
for _ in range(T):
    S = input()
    rule = input()

    for s in S:
        if s.isalpha():
            print(rule[ord(s) - ord('A')], end='')
        else:
            print(s, end='')
    print()