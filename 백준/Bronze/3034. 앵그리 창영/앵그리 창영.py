N, W, H = map(int, input().split())
WH = (W**2 + H**2)**0.5
for _ in range(N):
    match = int(input())
    if match <= W or match <= H or match <= WH:
        print('DA')
    else:
        print('NE')