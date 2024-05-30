N = int(input())
X, Y = 0, 0
for _ in range(N):
    winner = input()
    if winner == 'D':
        X += 1
    else:
        Y += 1

    if abs(X - Y) == 2:
        break

print('{}:{}'.format(X, Y))