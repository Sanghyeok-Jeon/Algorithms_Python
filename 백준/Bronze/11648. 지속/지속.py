happy = 0
target = int(input())
while True:
    if target < 10:
        break

    tmp_num = 1
    while target:
        tmp_num *= target % 10
        target //= 10

    happy += 1
    target = tmp_num

print(happy)