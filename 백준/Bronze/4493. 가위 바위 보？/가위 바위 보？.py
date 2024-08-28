T = int(input())
for _ in range(T):
    N = int(input())

    win_p1, win_p2 = 0, 0
    for _ in range(N):
        p1, p2 = input().split()
        if (p1, p2) == ('R', 'P'):
            win_p2 += 1
        elif (p1, p2) == ('R', 'S'):
            win_p1 += 1
        elif (p1, p2) == ('S', 'P'):
            win_p1 += 1
        elif (p1, p2) == ('S', 'R'):
            win_p2 += 1
        elif (p1, p2) == ('P', 'S'):
            win_p2 += 1
        elif (p1, p2) == ('P', 'R'):
            win_p1 += 1

    if win_p1 > win_p2:
        print('Player 1')
    elif win_p1 < win_p2:
        print('Player 2')
    else:
        print('TIE')