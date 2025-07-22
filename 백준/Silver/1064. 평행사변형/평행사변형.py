def is_possible():
    return (x2 - x1) * (y3 - y1) != (y2 - y1) * (x3 - x1)

def check_parallelogram():
    ab = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
    bc = ((y3 - y2) ** 2 + (x3 - x2) ** 2) ** 0.5
    ca = ((y1 - y3) ** 2 + (x1 - x3) ** 2) ** 0.5

    pl1 = ab * 2 + bc * 2
    pl2 = ab * 2 + ca * 2
    pl3 = bc * 2 + ca * 2

    return max(pl1, pl2, pl3) - min(pl1, pl2, pl3)


x1, y1, x2, y2, x3, y3 = map(int, input().split())

if not is_possible():
    print(-1.0)
else:
    print(check_parallelogram())