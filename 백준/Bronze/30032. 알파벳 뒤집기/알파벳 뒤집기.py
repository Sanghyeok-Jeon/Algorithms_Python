N, D = map(int, input().split())
dict_1 = {'d':'q', 'b':'p', 'q':'d', 'p':'b'}
dict_2 = {'d':'b', 'b':'d', 'q':'p', 'p':'q'}
for _ in range(N):
    origin_alpha = input()
    for a in origin_alpha:
        if D == 1:
            print(dict_1[a], end='')
        else:
            print(dict_2[a], end='')
    print()