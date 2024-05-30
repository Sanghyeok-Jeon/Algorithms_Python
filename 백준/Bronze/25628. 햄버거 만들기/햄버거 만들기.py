bread, patty = map(int, input().split())

cnt = 0
while True:
    if bread < 2 or patty < 1:
        break

    cnt += 1
    bread -= 2
    patty -= 1

print(cnt)