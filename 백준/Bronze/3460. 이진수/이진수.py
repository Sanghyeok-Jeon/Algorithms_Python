T = int(input())
for tc in range(T):
    n = int(input())
    for i in range(len(bin(n))-2):
        if n & 1 << i:
            print(i, end=' ')
    print()