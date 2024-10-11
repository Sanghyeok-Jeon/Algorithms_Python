A = input()
B = list(input().split())

for a in A:
    if a in B:
        print(a.lower(), end='')
    else:
        print(a, end='')