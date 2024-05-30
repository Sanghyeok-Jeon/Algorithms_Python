lv, verify = input().split()
if verify == 'miss':
    print(0)
elif verify == 'bad':
    print(200 * int(lv))
elif verify == 'cool':
    print(400 * int(lv))
elif verify == 'great':
    print(600 * int(lv))
else:
    print(1000 * int(lv))