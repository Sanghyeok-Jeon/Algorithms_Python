N = int(input())
for _ in range(N):
    S = input()

    total = 0
    for s in S:
        if s.isalpha():
            total += ord(s) - ord('A') + 1

    if total == 100:
        print('PERFECT LIFE')
    else:
        print(total)