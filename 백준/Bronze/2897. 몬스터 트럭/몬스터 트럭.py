R, C = map(int, input().split())
parking_lot = [input() for _ in range(R)]

zero_car, one_car, two_car, three_car, four_car = 0, 0, 0, 0, 0
for r in range(R - 1):
    for c in range(C - 1):
        two_by_two = (parking_lot[r][c]
                      + parking_lot[r][c + 1]
                      + parking_lot[r + 1][c]
                      + parking_lot[r + 1][c + 1])

        if '#' in two_by_two:
            continue

        cnt_X = two_by_two.count('X')
        if cnt_X == 0:
            zero_car += 1
        elif cnt_X == 1:
            one_car += 1
        elif cnt_X == 2:
            two_car += 1
        elif cnt_X == 3:
            three_car += 1
        else:
            four_car += 1

print(zero_car)
print(one_car)
print(two_car)
print(three_car)
print(four_car)