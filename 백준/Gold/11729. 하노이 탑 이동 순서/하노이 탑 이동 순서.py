def move_hanoi_tower(n, start, leavings, end):
    if n == 1:
        movingRecord.append((start, end))
        return

    move_hanoi_tower(n-1, start, end, leavings)
    movingRecord.append((start, end))
    move_hanoi_tower(n-1, leavings, start, end)

N = int(input())
movingRecord = []
move_hanoi_tower(N, 1, 2, 3)

print(len(movingRecord))
for mr in movingRecord:
    print(mr[0], mr[1])