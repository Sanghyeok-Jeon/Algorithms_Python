dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for _ in range(T):
    control_program = input()

    mode = 0
    x, y = 0, 0
    set_x = set()
    set_y = set()

    set_x.add(x)
    set_y.add(y)

    for c in control_program:
        if c == 'F':
            nx = x + dx[mode]
            ny = y + dy[mode]
            set_x.add(nx)
            set_y.add(ny)
            x, y = nx, ny
        elif c == 'B':
            nx = x - dx[mode]
            ny = y - dy[mode]
            set_x.add(nx)
            set_y.add(ny)
            x, y = nx, ny
        elif c == 'L':
            mode = (mode - 1) % 4
        else:
            mode = (mode + 1) % 4
            
    print((max(set_x) - min(set_x)) * (max(set_y) - min(set_y)))