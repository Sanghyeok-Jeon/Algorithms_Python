T = int(input())
for tc in range(T):
    A, B = input().split()

    if sorted(A) == sorted(B):
        print('{} & {} are anagrams.'.format(A, B))
    else:
        print('{} & {} are NOT anagrams.'.format(A, B))