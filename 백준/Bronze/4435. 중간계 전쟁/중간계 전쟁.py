T = int(input())
G = [1, 2, 3, 3, 4, 10]
S = [1, 2, 2, 2, 3, 5, 10]
for t in range(1, T+1):
    g_total = 0
    s_total = 0

    for i, v in enumerate(list(map(int, input().split()))):
        g_total += G[i] * v

    for i, v in enumerate(list(map(int, input().split()))):
        s_total += S[i] * v

    winner = ''
    if g_total > s_total:
        winner += 'Good triumphs over Evil'
    elif g_total < s_total:
        winner += 'Evil eradicates all trace of Good'
    else:
        winner += 'No victor on this battle field'

    print('Battle {}: {}'.format(t, winner))