def check_inside(x, y):
    if X <= x <= X + W and Y <= y <= Y + H:
        return True
    elif (X - x) ** 2 + (Y + R - y) ** 2 <= R ** 2:
        return True
    elif (X + W - x) ** 2 + (Y + R - y) ** 2 <= R ** 2:
        return True

    return False

W, H, X, Y, P = map(int, input().split())
members = [tuple(map(int, input().split())) for _ in range(P)]

R = H // 2

result = 0
for member in members:
    x, y = member

    if check_inside(x, y):
        result += 1

print(result)