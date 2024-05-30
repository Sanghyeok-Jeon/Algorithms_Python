typeShake = input()
ball = [1, 0, 0]
for ts in typeShake:
    if ts == 'A':
        ball[0], ball[1] = ball[1], ball[0]
    elif ts == 'B':
        ball[1], ball[2] = ball[2], ball[1]
    else:
        ball[0], ball[2] = ball[2], ball[0]
        
for i, v in enumerate(ball):
    if v:
        print(i+1)