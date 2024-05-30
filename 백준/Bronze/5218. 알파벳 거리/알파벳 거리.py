T = int(input())
for _ in range(T):
    alpha1, alpha2 = input().split()

    print('Distances:', end=' ')
    for i in range(len(alpha1)):
        a1 = ord(alpha1[i]) - ord('A') + 1
        a2 = ord(alpha2[i]) - ord('A') + 1
        if a1 <= a2:
            print(a2-a1, end=' ')
        else:
            print(a2+26-a1, end=' ')
    print()